"""Legendas provisórias da narração em português.
Cada bloco de narração do original (tempos medidos na Etapa 1, no playback) recebe os trechos correspondentes
do texto em português (narracao_texto_PT.pdf), divididos conforme as entradas e vozes de narracao-vozes.md.
Dentro de cada bloco, o tempo é repartido pelo número de caracteres. Refazer quando a gravação em PT existir.
Uso: python3 -I narracao.py <trechos.json> <saida.json>"""
import json, re, sys

# (compasso, voz, texto) por narração, lidos de um JSON fora do repositório (o texto da narração não é publicado):
# {"1": [[2, "M", "texto..."], ...], ...}
TRECHOS = {}
# blocos do narrador original (s, no playback; Etapa 1) e quais trechos em PT caem em cada um
BLOCOS = {
    1: [((3, 9), [0]), ((10, 17), [1]), ((22, 28), [2]), ((38, 46), [3])],
    2: [((8, 19), [0, 1]), ((23, 32), [2, 3])],
    3: [((12, 33), [0, 1, 2, 3])],
    4: [((11, 26), [0, 1, 2, 3]), ((27, 38), [4, 5])],
    5: [((5, 24), [0, 1]), ((25, 35), [2, 3, 4, 5])],
    6: [((9, 23), [0, 1, 2]), ((24, 32), [3, 4]), ((33, 37), [5])],
}
MAX = 80


def pedacos(txt):
    """Divide um texto em partes de tamanho parecido (até ~80 caracteres), cortando de preferência
    depois de pontuação e, senão, no espaço mais próximo da divisão igual."""
    import math
    k = math.ceil(len(txt) / MAX)
    if k <= 1:
        return [txt]
    alvo = len(txt) / k
    cortes, ini = [], 0
    for j in range(1, k):
        ideal = j * alvo
        forte = [m.end() for m in re.finditer(r"[;:.!?—]\s", txt) if ini + 15 < m.end() < len(txt) - 15]
        cand = [m.end() for m in re.finditer(r"[,]\s", txt) if ini + 15 < m.end() < len(txt) - 15]
        perto = [c for c in forte if abs(c - ideal) <= 25] or [c for c in cand if abs(c - ideal) <= 18]
        if perto:
            c = min(perto, key=lambda c: abs(c - ideal))
        else:
            esp = [m.start() + 1 for m in re.finditer(" ", txt) if ini + 10 < m.start() < len(txt) - 10]
            c = min(esp, key=lambda c: abs(c - ideal))
        cortes.append(c)
        ini = c
    partes, a = [], 0
    for c in cortes + [len(txt)]:
        partes.append(txt[a:c].strip())
        a = c
    return [p for p in partes if p]


def quebra_linhas(t):
    if len(t) <= 42:
        return [t]
    meio = len(t) // 2
    esp = [i for i, c in enumerate(t) if c == " "]
    pont = [i for i in esp if t[i - 1] in ",;:.!?" and abs(i - meio) <= 10]
    k = min(pont or esp, key=lambda i: abs(i - meio))
    return [t[:k], t[k + 1:]]


def gera():
    res = {}
    for n, blocos in BLOCOS.items():
        itens = []
        for (a, b), idx in blocos:
            # junta trechos consecutivos da mesma voz; corta sempre na troca de narrador
            corridas = []
            for i in idx:
                c, voz, txt = TRECHOS[n][i]
                if corridas and corridas[-1][1] == voz:
                    corridas[-1][2] += " " + txt
                else:
                    corridas.append([c, voz, txt])
            peds = []
            for c, voz, txt in corridas:
                pos = 0
                for p in pedacos(txt):
                    k = txt.find(p, pos)
                    pos = k + len(p)
                    # compasso: o do trecho original em que o pedaço começa
                    cc, acum = c, 0
                    for i in idx:
                        c2, v2, t2 = TRECHOS[n][i]
                        if v2 == voz and t2 in txt and txt.find(t2) <= k:
                            cc = c2
                    peds.append((cc, voz, p))
            tot = sum(len(p[2]) for p in peds)
            t = a
            for c, voz, p in peds:
                d = (b - a) * len(p) / tot
                itens.append(dict(ini=round(t, 2), fim=round(t + d, 2), texto=p, linhas=quebra_linhas(p),
                                  voz=voz, compasso=c, narracao=n))
                t += d
        res[n] = itens
    return res


if __name__ == "__main__":
    TRECHOS.update({int(k): [tuple(x) for x in v] for k, v in json.load(open(sys.argv[1])).items()})
    r = gera()
    json.dump(r, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
    for n, its in r.items():
        print(n, len(its), "itens; menor duração", min(round(i["fim"] - i["ini"], 1) for i in its), "s")
