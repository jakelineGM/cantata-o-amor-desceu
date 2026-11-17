"""Interpreta a geometria da v4: numera compassos, lê notas (altura MIDI) e sílabas da letra.
Uso: python3 -I interpretar_v4.py <v4_geo.json> <saida.json>"""
import json, sys, re
from collections import defaultdict

NOTEHEADS = {"œ": "preta", "˙": "branca", "w": "semibreve"}
ACC = {"#": 1, "b": -1, "n": 0}
SEMI = [0, 2, 4, 5, 7, 9, 11]
LETRA_LYR = ("PalatinoLinotype-Roman", "TeX Gyre Pagella Regular", "Palatino")


def is_music(c):
    return "Helsinki" in c["f"] and "Text" not in c["f"] and "Special" not in c["f"]


def is_lyric_font(c):
    preto = tuple(c["col"]) in ((0.0, 0.0, 0.0), (0, 0, 0))
    pal = "PalatinoLinotype-Roman" in c["f"] or "Pagella-Regular" in c["f"] or "Pagella Regular" in c["f"]
    elis = "HelsinkiTextStd" in c["f"] and c["t"] == "_"
    return preto and (pal or elis)


def diat(clef, y, st):
    passo = round((st["bot"] - y) / (st["sp"] / 2))
    return (30 if clef == "G" else 18) + passo     # E4 = 30, G2 = 18


def midi_de(d, alt):
    o, l = divmod(d, 7)
    return 12 * (o + 1) + SEMI[l] + alt


def palavras(chars):
    """Divide uma linha de letra em sílabas com posição própria.
    Cada sílaba: t (texto sem hífen), x, x1, hifen (continua na próxima sílaba), elisao (ligada à próxima palavra)."""
    chars = sorted(chars, key=lambda c: c["x"])
    toks = []
    for c in chars:
        if c["t"] == " ":
            continue
        novo = (not toks or c["x"] - toks[-1]["x1"] > 1.2 or toks[-1]["t"].endswith("-") or c["t"] == "_" or toks[-1]["t"] == "_"
                or c.get("sq") != toks[-1]["sq"])
        if novo:
            toks.append(dict(t=c["t"], x=c["x"], x1=c["x1"], y=c["y"], sq=c.get("sq")))
        else:
            toks[-1]["t"] += c["t"]
            toks[-1]["x1"] = c["x1"]
    res = []
    for tk in toks:
        if tk["t"] == "_":
            if res:
                res[-1]["elisao"] = True
            continue
        if set(tk["t"]) <= set("-–‐‑"):
            if res:
                res[-1]["hifen"] = True
            continue
        hif = tk["t"][-1] in "-‐‑"
        res.append(dict(t=tk["t"].rstrip("-‐‑"), x=tk["x"], x1=tk["x1"], y=tk["y"], hifen=hif, elisao=False))
    return res


def processa_sistema(sis, estado):
    out = dict(pagina=sis["pagina"], pautas=[], compassos=[], notas=[], silabas=[], textos=[])
    chars = sis["chars"]
    P = sis["pautas"]
    # números de compasso do início do sistema (Palatino pequeno, acima da 1ª pauta, à esquerda)
    st0 = P[0]
    nums = [c for c in chars if "Palatino" in c["f"] and st0["top"] - 22 < c["y"] < st0["top"] - 1 and c["x"] < st0["x0"] + 25 and c["t"].isdigit()]
    num_ini = None
    if nums:
        ymax_n = max(c["y"] for c in nums)
        nums = [c for c in nums if abs(c["y"] - ymax_n) < 1]
        num_ini = int("".join(c["t"] for c in sorted(nums, key=lambda c: c["x"])))
    # barras comuns: usa as da pauta com mais barras
    barras = [b for b in P[0]["barras"] if all(any(abs(b - b2) < 1.2 for b2 in p["barras"]) for p in P[1:])]
    x_ini = st0["x0"]
    segs = []
    lim = [x_ini] + [b for b in barras if b > x_ini + 3]
    if lim[-1] < st0["x1"] - 3:
        lim.append(st0["x1"])
    for a, b in zip(lim[:-1], lim[1:]):
        if b - a > 6:
            segs.append([a, b])
    # o 1º segmento costuma conter clave/armadura/fórmula + o 1º compasso
    # multicompassos: dígitos grandes Helsinki acima da pauta
    multi = defaultdict(int)
    for p in P:
        dig = [c for c in chars if is_music(c) and c["t"].isdigit() and c["y"] < p["top"] - 0.5 and c["y"] > p["top"] - 3 * p["sp"]]
        for si, (a, b) in enumerate(segs):
            ds = sorted([c for c in dig if a < c["x"] < b], key=lambda c: c["x"])
            if ds:
                multi[si] = max(multi[si], int("".join(c["t"] for c in ds)))
    if num_ini is None:
        num_ini = estado["prox"]
    n = num_ini
    for si, (a, b) in enumerate(segs):
        k = multi.get(si, 1) or 1
        out["compassos"].append(dict(n=n, x0=a, x1=b, qtd=k))
        n += k
    estado["prox"] = n
    # fórmulas de compasso: dígitos (ou 'c'/'C' de compasso comum) dentro da 1ª pauta
    ff = [c for c in chars if is_music(c) and (c["t"].isdigit() or c["t"] in "cC¢") and st0["top"] - 0.5 <= c["y"] <= st0["bot"] + 0.5]
    for cmp in out["compassos"]:
        dentro = sorted([c for c in ff if cmp["x0"] - 1 <= c["x"] <= cmp["x1"]], key=lambda c: (round(c["x"]), c["y"]))
        if not dentro:
            continue
        if dentro[0]["t"] in "cC":
            cmp["formula"] = [4, 4]
            continue
        if dentro[0]["t"] == "¢":
            cmp["formula"] = [2, 2]
            continue
        x0 = dentro[0]["x"]
        col = [c for c in dentro if abs(c["x"] - x0) < 6]
        ys = sorted(set(round(c["y"]) for c in col))
        if len(ys) >= 2:
            cima = "".join(c["t"] for c in sorted(col, key=lambda c: c["x"]) if round(c["y"]) == ys[0])
            baixo = "".join(c["t"] for c in sorted(col, key=lambda c: c["x"]) if round(c["y"]) == ys[-1])
            cmp["formula"] = [int(cima), int(baixo)]
    # pautas: clave e armadura
    for pi, p in enumerate(P):
        ymin = p["top"] - 7 * p["sp"]
        ymax = (P[pi + 1]["top"] - 2.5 * p["sp"]) if pi + 1 < len(P) else p["bot"] + 7 * p["sp"]
        mus = [c for c in chars if is_music(c) and ymin <= c["y"] <= ymax]
        claves = sorted([(c["x"], "G" if c["t"] == "&" else "F") for c in mus if c["t"] in "&?" and p["top"] - 1 <= c["y"] <= p["bot"] + 1])
        if not claves:
            claves = [(p["x0"], estado["clave"].get(pi, "G"))]
        estado["clave"][pi] = claves[-1][1]

        def clave_em(x):
            cl = claves[0][1]
            for cx, ct in claves:
                if cx <= x + 0.5:
                    cl = ct
            return cl
        heads = [c for c in mus if c["t"] in NOTEHEADS]
        accs = [c for c in mus if c["t"] in ACC and p["top"] - 4 * p["sp"] <= c["y"] <= p["bot"] + 4 * p["sp"]]
        # acidente de nota: há cabeça logo à direita na mesma altura
        armadura_ev = []   # (x, {letra: alt}) mudanças de armadura
        acc_nota = []
        grupo = []
        for c in sorted(accs, key=lambda c: c["x"]):
            alvo = [h for h in heads if 1.5 < h["x"] - c["x"] < 4.2 * p["sp"] and abs(h["y"] - c["y"]) < 0.6 * p["sp"]]
            if alvo:
                acc_nota.append((c, min(alvo, key=lambda h: h["x"] - c["x"])))
            else:
                grupo.append(c)
        # agrupa glifos de armadura contíguos
        blocos = []
        for c in grupo:
            if blocos and c["x"] - blocos[-1][-1]["x"] < 2.6 * p["sp"]:
                blocos[-1].append(c)
            else:
                blocos.append([c])
        arm0 = estado["arm"].get(pi, {})
        evs = []
        for bl in blocos:
            nova = {}
            for c in bl:
                if c["t"] in "#b":
                    l = diat(clave_em(c["x"]), c["y"], p) % 7
                    nova[l] = ACC[c["t"]]
            evs.append((bl[0]["x"], nova))
        if not evs or evs[0][0] > p["x0"] + 6 * p["sp"] + 20:
            evs.insert(0, (p["x0"], arm0))
        estado["arm"][pi] = evs[-1][1]

        def arm_em(x):
            a = evs[0][1]
            for ex, ea in evs:
                if ex <= x + 0.5:
                    a = ea
            return a
        accmap = {id(h): ACC[c["t"]] for c, h in acc_nota}
        # notas com acidentes de compasso
        notas = []
        for h in sorted(heads, key=lambda h: h["x"]):
            seg = next((cmp for cmp in out["compassos"] if cmp["x0"] - 0.5 <= h["x"] <= cmp["x1"]), None)
            if seg is None:
                continue
            d = diat(clave_em(h["x"]), h["y"], p)
            notas.append(dict(h=h, d=d, seg=seg))
        vigente = {}
        for nt in notas:
            h, d, seg = nt["h"], nt["d"], nt["seg"]
            chave = (seg["n"], d)
            if id(h) in accmap:
                vigente[chave] = accmap[id(h)]
            alt = vigente.get(chave, arm_em(h["x"]).get(d % 7, 0))
            out["notas"].append(dict(pauta=pi, compasso=seg["n"], frac=round((h["x"] - seg["x0"]) / max(seg["x1"] - seg["x0"], 1), 4),
                                     x=round(h["x"], 2), y=round(h["y"], 2), midi=midi_de(d, alt), tipo=NOTEHEADS[h["t"]]))
        # letra: linhas abaixo da pauta
        lyr = [c for c in chars if is_lyric_font(c) and p["bot"] + 1.5 * p["sp"] <= c["y"] <= (ymax + 2 * p["sp"])
               and c["s"] < 13]
        linhas_y = []
        for c in sorted(lyr, key=lambda c: c["y"]):
            if linhas_y and abs(c["y"] - linhas_y[-1][0]) < 2.5:
                linhas_y[-1][1].append(c)
            else:
                linhas_y.append([c["y"], [c]])
        linhas_y = [(ly, cs) for ly, cs in linhas_y if not any(c["t"] == "©" for c in cs)
                    and "Lorenz" not in "".join(c["t"] for c in sorted(cs, key=lambda c: c["x"]))
                    and "direitos" not in "".join(c["t"] for c in sorted(cs, key=lambda c: c["x"]))]
        for li, (ly, cs) in enumerate(linhas_y):
            for w in palavras(cs):
                cx = (w["x"] + w["x1"]) / 2
                seg = next((cmp for cmp in out["compassos"] if cmp["x0"] - 2 <= w["x"] <= cmp["x1"] + 2), None)
                if seg is None:
                    continue
                out["silabas"].append(dict(pauta=pi, linha=li, y=round(ly, 1), t=w["t"], hifen=w["hifen"], elisao=w["elisao"], x=round(w["x"], 2), x1=round(w["x1"], 2),
                                           compasso=seg["n"], frac=round((w["x"] - seg["x0"]) / max(seg["x1"] - seg["x0"], 1), 4)))
        out["pautas"].append(dict(top=p["top"], bot=p["bot"], clave=claves[0][1], armadura=evs[0][1]))
    # textos (andamentos, indicações): Palatino/Pagella acima da 1ª pauta
    tx = [c for c in chars if not is_music(c) and c["y"] < st0["top"] - 1]
    linhas_t = defaultdict(list)
    for c in tx:
        linhas_t[round(c["y"] / 3)].append(c)
    for k, cs in linhas_t.items():
        for w in palavras(cs):
            seg = next((cmp for cmp in out["compassos"] if cmp["x0"] - 5 <= w["x"] <= cmp["x1"]), None)
            out["textos"].append(dict(t=w["t"], x=round(w["x"], 2), compasso=seg["n"] if seg else None))
    return out


if __name__ == "__main__":
    geo = json.load(open(sys.argv[1]))
    res = {}
    for m, sistemas in geo.items():
        estado = dict(prox=1, clave={}, arm={})
        res[m] = [processa_sistema(s, estado) for s in sistemas]
        for a, b in zip(res[m][:-1], res[m][1:]):
            ini = b["compassos"][0]["n"]
            while a["compassos"] and a["compassos"][-1]["n"] >= ini:
                cut = a["compassos"].pop()
                a["notas"] = [n for n in a["notas"] if n["x"] < cut["x0"] - 0.5]
                a["silabas"] = [x for x in a["silabas"] if x["x"] < cut["x0"] - 2]
        ult = res[m][-1]["compassos"][-1]
        print("musica", m, "compassos ate", ult["n"] + ult["qtd"] - 1, "notas", sum(len(s["notas"]) for s in res[m]),
              "silabas", sum(len(s["silabas"]) for s in res[m]))
    json.dump(res, open(sys.argv[2], "w"), ensure_ascii=False, indent=0)
