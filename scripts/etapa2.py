"""Monta a Etapa 2: versos em português com tempo, sinalizações de prosódia e legendas .srt.
Uso: python3 -I etapa2.py <v4_score.json> <alinhamento.json> <mapa-de-tempos.json> <pasta_saida>
Em cada sílaba: 'txt' = texto, 'tempo' = segundos no playback da faixa."""
import json, sys, re, os, unicodedata
import numpy as np
from spellchecker import SpellChecker

DIC = SpellChecker(language="pt")

SLUG = {1: "01_o-amor-desceu", 2: "02_vem-emanuel-vem", 3: "03_da-nos-paz", 4: "04_ouca-a-alegre-cancao",
        5: "05_o-amor-seja-seu-e-meu", 6: "06_amor-divino"}
ORDEM_VOZ = {"Desc": 0, "M": 1, "H": 2}
LEAD = 0.25          # legenda aparece um pouco antes do canto
HOLD = 0.4           # e fica um pouco depois da última nota
MAX_CHARS = 46
DUR_Q = {"preta": 1, "branca": 2, "semibreve": 4}
CURTAS = {"o", "a", "e", "de", "do", "da", "no", "na", "em", "eu", "se", "te", "me", "ao", "os", "as", "um", "ti", "tu", "la",
          "e", "es", "ja", "so", "ha", "oh", "ve", "fe", "da", "a", "as", "ou", "vos", "nos", "ja"}
LATIM = {"dona", "nobis", "pacem", "excelsis", "deo", "gloria in"}


def mapa_suave(comps):
    """Tempo de início de cada compasso: mediana das previsões dos vizinhos (remove barras mal alinhadas)."""
    ks = sorted(int(k) for k in comps)
    T = np.array([comps[str(k)]["tn"] for k in ks])
    B = np.array([comps[str(k)]["t_cant"] for k in ks])
    Bs = B.copy()
    n = len(ks)
    for i in range(n):
        lo, hi = max(0, i - 3), min(n, i + 4)
        rs = [(B[j + 1] - B[j]) / max(T[j + 1] - T[j], 1e-6) for j in range(lo, min(hi, n - 1))]
        R = float(np.median(rs)) if rs else 1.0
        Bs[i] = float(np.median([B[j] + (T[i] - T[j]) * R for j in range(lo, hi)]))
    Bs = np.maximum.accumulate(Bs)
    return {k: (T[i], Bs[i]) for i, k in enumerate(ks)}


def tempo_sil(x, ms, comps):
    k = x["compasso"]
    tn0, b0 = ms[k]
    if k + 1 in ms:
        tn1, b1 = ms[k + 1]
    else:
        tn1, b1 = tn0 + comps[str(k)]["dur_n"], b0 + comps[str(k)]["dur_n"]
    esc = (b1 - b0) / max(tn1 - tn0, 1e-6)
    return b0 + (x["tn"] - tn0) * esc, esc


def tonica(sils):
    s = [re.sub(r"[^\wáéíóúâêôãõàüç]", "", unicodedata.normalize("NFKC", x).lower()) for x in sils]
    if len(s) < 2 or not all(s):
        return None
    for i, x in enumerate(s):
        if re.search("[áéíóúâêô]", x):
            return i
    for i, x in enumerate(s):
        if re.search("[ãõ]", x):
            return i
    w = "".join(s)
    if re.search(r"(r|l|z|x|i|is|u|us|im|ins|um|uns|om|ons)$", w) and not re.search(r"(qui|gui|que|gue)$", w):
        return len(s) - 1
    return len(s) - 2


def peso_metrico(beat, quartos, formula):
    """3 = cabeça do compasso, 2 = tempo forte secundário, 1 = tempo, 0 = contratempo."""
    b = round(beat * 2) / 2
    if abs(b) < 0.26:
        return 3
    if formula == [6, 8] and abs(b - 1.5) < 0.26:
        return 2
    if formula in ([4, 4], [2, 2]) and abs(b - 2) < 0.26:
        return 2
    if abs(b - round(b)) < 0.01 and formula not in ([6, 8], [3, 8]):
        return 1
    return 0


def rotulo_voz(sis, pauta):
    claves = [p["clave"] for p in sis["pautas"]]
    if claves[pauta] == "F":
        return "H"
    if claves.count("G") >= 2 and pauta == 0:
        return "Desc"
    return "M"


def palavras_de(stream):
    pal, cur = [], []
    for x in stream:
        cur.append(x)
        if not x.get("hifen"):
            pal.append(cur)
            cur = []
    if cur:
        pal.append(cur)
    return pal


ENCLITICOS = {"nos", "vos", "se", "lhe", "lhes"}
COM_HIFEN = {"unase"}


def palavra(w):
    """Junta as sílabas; mantém o hífen de pronome oblíquo (dá-nos, chegai-vos, una-se)."""
    txt = unicodedata.normalize("NFKC", "".join(s["txt"] for s in w))
    if len(w) >= 2:
        ult = norm(w[-1]["txt"])
        antes = unicodedata.normalize("NFC", w[-2]["txt"].lower())
        base = "".join(s["txt"] for s in w[:-1])
        if ult in ENCLITICOS and (re.search(r"[áéêóíô]$|[aeiou][iu]$|r$", antes) or norm(txt) in COM_HIFEN):
            txt = unicodedata.normalize("NFKC", base + "-" + w[-1]["txt"])
    return txt


def texto(pal):
    return re.sub(r"\s+", " ", " ".join(palavra(w) for w in pal)).strip()


def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    return re.sub(r"[^a-z ]", "", "".join(c for c in t if unicodedata.category(c) != "Mn")).strip()


def frases_do_stream(stream, beat_s):
    pal = palavras_de(stream)
    frases, cur = [], []
    for w in pal:
        if cur:
            ult = cur[-1][-1]
            gap = w[0]["tempo"] - ult["tempo"]
            q = beat_s(ult)
            forte = re.search(r"[.!?;:]$", ult["txt"])
            virg = ult["txt"].endswith(",")
            if gap >= 3.2 * q or (forte and gap >= 1.4 * q) or (virg and gap >= 2.2 * q and len(texto(cur)) > 14):
                frases.append(cur)
                cur = []
        cur.append(w)
    if cur:
        frases.append(cur)
    res, pilha = [], list(frases)
    while pilha:
        g = pilha.pop(0)
        if len(texto(g)) <= MAX_CHARS or len(g) < 4:
            res.append(g)
            continue
        meio = len(texto(g)) / 2
        melhor, mk = 1, 1e9
        for k in range(1, len(g)):
            pen = abs(len(texto(g[:k])) - meio) - (12 if re.search(r"[,;:.!?]$", g[k - 1][-1]["txt"]) else 0)
            if pen < mk:
                mk, melhor = pen, k
        pilha[0:0] = [g[:melhor], g[melhor:]]
    return res


def citacoes_de(sist):
    out = []
    for s in sist:
        toks = s["textos"]
        for i, tk in enumerate(toks):
            if tk["t"].startswith("*"):
                j = i + 1
                while j < len(toks) and not toks[j]["t"].startswith("*") and not re.match(r"^([q=]|\d+)$", toks[j]["t"]) and j - i < 8:
                    j += 1
                titulo = " ".join(t["t"] for t in toks[i:j]).lstrip("*")
                titulo = re.split(r"\s+(?=Com |Grandioso|Misterioso|Calmamente|Ternamente|Decidido|Leve |Tranquilo|Joel )", titulo)[0]
                out.append(dict(compasso=tk["compasso"], titulo=titulo.strip()))
    return out


def vocabulario(score):
    """Palavras com mais de uma sílaba (hifenizadas na partitura) e palavras que aparecem sozinhas."""
    multi, sozinha = set(), set()
    for sist in score.values():
        for s in sist:
            linhas = {}
            for x in s["silabas"]:
                linhas.setdefault((x["pauta"], x["linha"]), []).append(x)
            for ls in linhas.values():
                ls.sort(key=lambda x: x["x"])
                cur = []
                for x in ls:
                    cur.append(x)
                    if not x["hifen"]:
                        w = norm("".join(y["t"] for y in cur))
                        (multi if len(cur) > 1 else sozinha).add(w)
                        cur = []
    return multi, sozinha


def juntar_hifens_omitidos(streams, vocab):
    """A partitura omite alguns hífens (fim de sistema e sílabas apertadas). Junta A + B quando a junção forma
    uma palavra que existe (na própria letra, hifenizada, ou no dicionário) e A ou B sozinho não é palavra comum."""
    multi, _ = vocab
    freq = DIC.word_frequency
    for st in streams.values():
        for i in range(len(st) - 1):
            a = st[i]
            if a.get("hifen") or a.get("elisao") or re.search(r"[,.;:!?]$", a["txt"]):
                continue
            j = i
            while j > 0 and st[j - 1].get("hifen"):
                j -= 1
            pref = "".join(s["txt"] for s in st[j:i + 1])        # a palavra inteira que termina em a
            k, w, bw = i + 1, pref, ""
            while k < len(st):
                w += st[k]["txt"]
                bw += st[k]["txt"]
                if not st[k].get("hifen"):
                    break
                k += 1
            W = norm(w)
            A, B = norm(pref), norm(bw)
            if bw[:1].isupper():
                continue
            if W in multi or (freq[W] >= 50 and min(freq[A], freq[B]) < 100):
                a["hifen"] = True


def processa(m, score, al):
    sist = score[str(m)]
    r = al[str(m)]
    comps = r["compassos"]
    ms = mapa_suave(comps)
    off = r["silabas"][0]["t_pb"] - r["silabas"][0]["t_cant"]
    formulas, form = {}, [4, 4]
    for s in sist:
        for c in s["compassos"]:
            form = c.get("formula", form)
            for k in range(c["qtd"]):
                formulas[c["n"] + k] = form
    streams = {}
    for x in r["silabas"]:
        if x["compasso"] not in ms:
            continue
        t, esc = tempo_sil(x, ms, comps)
        y = dict(x, voz=rotulo_voz(sist[x["sis"]], x["pauta"]), txt=x["t"], tempo=t + off, esc=esc)
        streams.setdefault((y["voz"], x["linha"]), []).append(y)
    # marca a última sílaba de cada linha de letra de cada sistema
    ultimas = {}
    for st in streams.values():
        for y in st:
            k = (y["sis"], y["pauta"], y["linha"])
            if k not in ultimas or y["x"] > ultimas[k]["x"]:
                ultimas[k] = y
    for y in ultimas.values():
        y["fim_linha"] = True
    for st in streams.values():
        st.sort(key=lambda y: (y["tempo"], y["x"]))
    juntar_hifens_omitidos(streams, VOCAB)

    def beat_s(y):
        return comps[str(y["compasso"])]["q"] * y["esc"]
    frases = []
    for (voz, lin), st in streams.items():
        for f in frases_do_stream(st, beat_s):
            sils = [s for w in f for s in w]
            ult = sils[-1]
            fim = ult["tempo"] + max(DUR_Q.get(ult.get("tipo", "preta"), 1) * beat_s(ult), 0.5)
            frases.append(dict(voz=voz, linha=lin, ini=sils[0]["tempo"], fim=fim, texto=texto(f), pal=f,
                               c_ini=sils[0]["compasso"], c_fim=ult["compasso"]))
    frases.sort(key=lambda f: (f["ini"], ORDEM_VOZ[f["voz"]]))
    grupos = []
    for f in frases:
        g = grupos[-1] if grupos else None
        if g and (min(f["fim"], g["fim"]) - max(f["ini"], g["ini"])) > 0.35 * min(f["fim"] - f["ini"], g["fim"] - g["ini"]):
            g["frases"].append(f)
            g["ini"], g["fim"] = min(g["ini"], f["ini"]), max(g["fim"], f["fim"])
        else:
            grupos.append(dict(ini=f["ini"], fim=f["fim"], frases=[f]))
    for g in grupos:
        textos, vozes = [], []
        for f in sorted(g["frases"], key=lambda f: ORDEM_VOZ[f["voz"]]):
            n = norm(f["texto"])
            ja = next((k for k, t in enumerate(textos) if norm(t) == n or (len(n) > 6 and n in norm(t))), None)
            if ja is None:
                textos.append(f["texto"])
                vozes.append({f["voz"]})
            else:
                vozes[ja].add(f["voz"])
        g["linhas"] = textos[:3]
        g["vozes"] = ["+".join(sorted(v, key=ORDEM_VOZ.get)) for v in vozes]
        g["extra"] = textos[3:]
        g["c_ini"] = min(f["c_ini"] for f in g["frases"])
        g["c_fim"] = max(f["c_fim"] for f in g["frases"])
    # junta fragmentos curtos (1-2 palavras) à frase anterior da mesma voz quando a frase anterior não terminou
    j = 1
    while j < len(grupos):
        a_, b_ = grupos[j - 1], grupos[j]
        if (len(a_["linhas"]) == 1 and len(b_["linhas"]) == 1 and a_["vozes"] == b_["vozes"]
                and len(b_["linhas"][0].split()) <= 2 and not re.search(r"[.!?;:]$", a_["linhas"][0])
                and b_["ini"] - a_["fim"] < 6):
            a_["linhas"][0] += " " + b_["linhas"][0]
            a_["fim"], a_["c_fim"] = b_["fim"], b_["c_fim"]
            a_["frases"] += b_["frases"]
            grupos.pop(j)
        else:
            j += 1
    # palavra solta (1 palavra, < 1 s) logo antes do verso seguinte: passa para o começo dele
    j = 0
    while j < len(grupos) - 1:
        a_, b_ = grupos[j], grupos[j + 1]
        if len(a_["linhas"]) == 1 and len(a_["linhas"][0].split()) == 1 and a_["fim"] - a_["ini"] < 1.0 \
                and b_["ini"] - a_["ini"] < 1.0:
            b_["linhas"][0] = a_["linhas"][0] + " " + b_["linhas"][0]
            b_["ini"], b_["c_ini"] = a_["ini"], a_["c_ini"]
            b_["frases"] = a_["frases"] + b_["frases"]
            grupos.pop(j)
        else:
            j += 1
    # prosódia: sílaba tônica em tempo fraco com átona da mesma palavra na cabeça do compasso
    sinal, vistos = [], set()
    for f in frases:
        for w in f["pal"]:
            sils = [s["txt"] for s in w]
            ti = tonica(sils)
            if ti is None:
                continue
            pesos = []
            for s in w:
                cm = comps[str(s["compasso"])]
                fm = formulas.get(s["compasso"], [4, 4])
                pesos.append(peso_metrico((s["tn"] - cm["tn"]) / cm["q"], fm[0] * 4 / fm[1], fm))
            if norm("".join(sils)) in LATIM:
                continue
            # sílabas com acento secundário (2, 4... antes da tônica) podem cair na cabeça do compasso
            atonas = [p for i, p in enumerate(pesos) if i != ti and not (i < ti and (ti - i) % 2 == 0)]
            if atonas and max(atonas) >= 3 and pesos[ti] <= 1:
                chave = (w[0]["compasso"], norm("".join(sils)))
                if chave in vistos:
                    continue
                vistos.add(chave)
                i_forte = next(i for i, p in enumerate(pesos) if i != ti and not (i < ti and (ti - i) % 2 == 0) and p == max(atonas))
                limpa = lambda z: z.strip(",.;:!?")
                sinal.append(dict(compasso=w[0]["compasso"], voz=f["voz"], palavra="-".join(limpa(z) for z in sils),
                                  tonica=limpa(sils[ti]), forte=limpa(sils[i_forte]), tempo=round(w[0]["tempo"], 2)))
    elisoes = []
    for st in streams.values():
        for i, y in enumerate(st):
            if y.get("elisao") and i + 1 < len(st):
                elisoes.append(dict(compasso=y["compasso"], voz=y["voz"], txt=f"{y['txt']}_{st[i + 1]['txt']}"))
    return dict(grupos=grupos, sinal=sinal, citacoes=citacoes_de(sist), elisoes=elisoes, off=off)


def ts(t):
    t = max(t, 0)
    h, rem = divmod(int(round(t * 1000)), 3600000)
    mi, rem = divmod(rem, 60000)
    s, ms = divmod(rem, 1000)
    return f"{h:02d}:{mi:02d}:{s:02d},{ms:03d}"


def itens(grupos, base=0.0, conferencia=False):
    out = []
    for i, g in enumerate(grupos):
        ini = g["ini"] - LEAD
        fim = g["fim"] + HOLD
        if i + 1 < len(grupos):
            fim = min(fim, grupos[i + 1]["ini"] - LEAD - 0.05)
        fim = max(fim, ini + 0.8)
        if i + 1 < len(grupos):
            fim = min(fim, grupos[i + 1]["ini"] - LEAD - 0.05)
        linhas = list(g["linhas"])
        if conferencia:
            linhas = [f"{l}  ({v})" for l, v in zip(g["linhas"], g["vozes"])] + [f"[c. {g['c_ini']}–{g['c_fim']}]"]
        out.append((ini + base, fim + base, linhas))
    return out


def itens_narracao(narr, base=0.0, conferencia=False):
    out = []
    for it in narr:
        if conferencia:
            linhas = it["linhas"] + [f"[Narração {it['narracao']} · voz {it['voz']} · c. {it['compasso']} · tempo provisório]"]
        else:
            linhas = [f"<i>{l}</i>" for l in it["linhas"]]
        out.append((it["ini"] + base, it["fim"] + base, linhas))
    return out


def srt(items):
    return "\n".join(f"{i}\n{ts(a)} --> {ts(b)}\n" + "\n".join(ls) + "\n" for i, (a, b, ls) in enumerate(items, 1))


if __name__ == "__main__":
    score = json.load(open(sys.argv[1]))
    al = json.load(open(sys.argv[2]))
    VOCAB = vocabulario(score)
    mapa = json.load(open(sys.argv[3]))
    outdir = sys.argv[4]
    os.makedirs(f"{outdir}/legendas", exist_ok=True)
    ini_global = {f["faixa"]: f["linha_do_tempo"]["inicio_s"] for f in mapa["faixas"]}
    narr = json.load(open(sys.argv[5])) if len(sys.argv) > 5 else {}
    todos, todos_c, dump = [], [], {}
    for m in range(1, 7):
        r = processa(m, score, al)
        nm = narr.get(str(m), [])
        pt = sorted(itens_narracao(nm) + itens(r["grupos"]))
        cf = sorted(itens_narracao(nm, conferencia=True) + itens(r["grupos"], conferencia=True))
        open(f"{outdir}/legendas/{SLUG[m]}_PT.srt", "w", encoding="utf-8").write(srt(pt))
        open(f"{outdir}/legendas/{SLUG[m]}_conferencia.srt", "w", encoding="utf-8").write(srt(cf))
        todos += [(a + ini_global[m], b + ini_global[m], l) for a, b, l in pt]
        todos_c += [(a + ini_global[m], b + ini_global[m], l) for a, b, l in cf]
        dump[m] = dict(grupos=[{k: v for k, v in g.items() if k != "frases"} for g in r["grupos"]], sinal=r["sinal"],
                       citacoes=r["citacoes"], elisoes=r["elisoes"], narracao=nm)
        print(m, "legendas", len(r["grupos"]), "prosódia", len(r["sinal"]), "elisões", len(r["elisoes"]),
              "citações", [c["titulo"] for c in r["citacoes"]])
    open(f"{outdir}/legendas/00_cantata-completa_PT.srt", "w", encoding="utf-8").write(srt(todos))
    open(f"{outdir}/legendas/00_cantata-completa_conferencia.srt", "w", encoding="utf-8").write(srt(todos_c))
    json.dump(dump, open(f"{outdir}/etapa2.json", "w"), ensure_ascii=False, indent=1, default=float)
