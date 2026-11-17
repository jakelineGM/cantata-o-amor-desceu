"""Extrai da partitura vetorial v4 (Sibelius) a geometria de cada sistema: pautas, barras e caracteres visíveis.
Uso: python3 -I extrair_v4.py <v4.pdf> <saida.json>"""
import json, sys
import pymupdf

PAGINAS = {1: range(4, 9), 2: range(9, 16), 3: range(16, 21), 4: range(21, 28), 5: range(28, 34), 6: range(34, 40)}
WHITE = (1.0, 1.0, 1.0)


def visiveis(page):
    """Caracteres visíveis (origem x, y da linha de base) depois de aplicar as camadas brancas."""
    tt = page.get_texttrace()
    dr = page.get_drawings()
    brancos_rect = [(d["seqno"], d["rect"]) for d in dr if d.get("fill") == WHITE]
    chars = []
    for sp in tt:
        for c in sp["chars"]:
            chars.append(dict(t=chr(c[0]), x=c[2][0], y=c[2][1], bbox=c[3], font=sp["font"],
                              size=sp["size"], color=tuple(round(v, 3) for v in sp["color"]), seq=sp["seqno"]))
    brancos_glifo = [c for c in chars if c["color"] == WHITE]
    vis = []
    for c in chars:
        if c["color"] == WHITE:
            continue
        hidden = any(g["seq"] > c["seq"] and g["t"] == c["t"] and abs(g["x"] - c["x"]) < 0.4 and abs(g["y"] - c["y"]) < 0.4
                     for g in brancos_glifo)
        if not hidden:
            cx = (c["bbox"][0] + c["bbox"][2]) / 2
            cy = c["y"] - 1
            hidden = any(s > c["seq"] and r.x0 - 0.2 <= cx <= r.x1 + 0.2 and r.y0 - 0.5 <= cy <= r.y1 + 0.5
                         for s, r in brancos_rect)
        if not hidden:
            vis.append(c)
    return vis, dr


def linhas(dr):
    hs, vs = [], []
    for d in dr:
        if d.get("fill") == WHITE:
            continue
        w = d.get("width") or 0
        for it in d["items"]:
            if it[0] == "l":
                p1, p2 = it[1], it[2]
                if abs(p1.y - p2.y) < 0.3 and abs(p1.x - p2.x) > 60:
                    hs.append((min(p1.x, p2.x), max(p1.x, p2.x), p1.y, w))
                elif abs(p1.x - p2.x) < 0.3 and abs(p1.y - p2.y) > 8:
                    vs.append((p1.x, min(p1.y, p2.y), max(p1.y, p2.y), w))
            elif it[0] == "re" and d.get("fill") and d["fill"] != WHITE:
                r = it[1]
                if r.width < 3 and r.height > 8:      # barra desenhada como retângulo fino
                    vs.append(((r.x0 + r.x1) / 2, r.y0, r.y1, r.width))
    return hs, vs


def pautas(hs):
    ys = sorted(set(round(h[2], 2) for h in hs))
    res, i = [], 0
    while i + 4 < len(ys):
        g = ys[i:i + 5]
        dif = [g[k + 1] - g[k] for k in range(4)]
        if max(dif) - min(dif) < 0.3 and 3 < dif[0] < 6:
            x0 = min(h[0] for h in hs if abs(h[2] - g[0]) < 0.3)
            x1 = max(h[1] for h in hs if abs(h[2] - g[0]) < 0.3)
            res.append(dict(top=g[0], bot=g[4], sp=(g[4] - g[0]) / 4, x0=x0, x1=x1))
            i += 5
        else:
            i += 1
    return res


def processa(pdf, musica):
    sistemas = []
    for pn in PAGINAS[musica]:
        page = pdf[pn - 1]
        ch, dr = visiveis(page)
        hs, vs = linhas(dr)
        st = pautas(hs)
        grossos = [v for v in vs if v[3] > 1.2 and v[2] - v[1] > 30]
        grupos = []
        for s in st:
            juntou = False
            if grupos:
                g = grupos[-1]
                if any(v[1] - 1.5 <= g[0]["top"] and s["bot"] <= v[2] + 1.5 for v in grossos):
                    g.append(s)
                    juntou = True
            if not juntou:
                grupos.append([s])
        for g in grupos:
            sis = dict(pagina=pn, pautas=[])
            for k, s in enumerate(g):
                s = dict(s, i=k)
                bx = sorted(v[0] for v in vs if 0.6 < v[3] < 1.6 and abs(v[1] - s["top"]) < 1.5 and abs(v[2] - s["bot"]) < 1.5)
                bx += sorted(v[0] for v in vs if v[3] >= 1.6 and v[1] <= s["top"] + 1 and v[2] >= s["bot"] - 1 and v[0] > s["x0"] + 20)
                bxs = []
                for x in sorted(bx):
                    if bxs and x - bxs[-1] < 5:
                        bxs[-1] = x
                    else:
                        bxs.append(x)
                s["barras"] = [round(x, 2) for x in bxs]
                sis["pautas"].append(s)
            ytop, ybot = g[0]["top"], g[-1]["bot"]
            prox = [s2 for s2 in st if s2["top"] > ybot]
            ylim = (prox[0]["top"] - 25) if prox else ybot + 70
            sis["ylim"] = [ytop - 45, ylim]
            sis["chars"] = [dict(t=c["t"], x=round(c["x"], 2), y=round(c["y"], 2), x1=round(c["bbox"][2], 2), f=c["font"],
                                 s=round(c["size"], 2), col=c["color"], sq=c["seq"])
                            for c in ch if ytop - 45 <= c["y"] <= ylim]
            sistemas.append(sis)
    return sistemas


if __name__ == "__main__":
    pdf = pymupdf.open(sys.argv[1])
    out = {m: processa(pdf, m) for m in PAGINAS}
    json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False)
    for m, ss in out.items():
        print(m, len(ss), [len(s["pautas"]) for s in ss])
