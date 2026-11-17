"""Alinha a partitura v4 (notas e sílabas) com a voz isolada da gravação cantada, por DTW de croma.
Uso: python3 -I alinhar.py <v4_score.json> <pasta_cantadas> <pasta_playbacks> <saida.json>
Saída por música: tempo (s, na faixa cantada e no playback) de cada sílaba e de cada compasso."""
import json, subprocess, sys
import numpy as np
from numba import njit

SR = 22050
FPS = 20
HOP = SR // FPS
CANT = {1: "01_o_amor_desceu_cantado.mpeg", 2: "02_vem_emanuel_cantada.mpeg", 3: "03_da_nos_paz_cantado.mpeg",
        4: "04_ouca_a_alegre_cancao_cantado.mpeg", 5: "05_o_amor_seja_seu_e_meu_cantada.mpeg", 6: "06_amor_divino_cantada.mpeg"}
PB = {1: "01_o-amor-desceu_playback.mp3", 2: "02_vem-emanuel-vem_playback.mp3", 3: "03_da-nos-paz_playback.mp3",
      4: "04_ouca-a-alegre-cancao_playback.mp3", 5: "05_o-amor-seja-seu-e-meu_playback.mp3", 6: "06_amor-divino_playback.mp3"}
OFFSET = {1: 0.228, 2: 0.427, 3: 0.429, 4: 0.435, 5: 0.4306, 6: 0.4399}
# entrada do texto cantado: (compasso, tempo na faixa cantada, s)
ENTRADA = {1: (22, 46.80), 2: (29, 60.10), 3: (25, 47.97), 4: (24, 50.77), 5: (13, 36.70), 6: (20, 38.50)}
DUR_TIPO = {"preta": 1.0, "branca": 2.0, "semibreve": 4.0}


def load(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def residuo(m, dcant, dpb):
    s = load(f"{dcant}/{CANT[m]}")
    x = load(f"{dpb}/{PB[m]}")
    off = int(round(OFFSET[m] * SR))
    xs = np.zeros_like(s)
    seg = x[off: off + len(s)]
    xs[: len(seg)] = seg
    g = float(np.dot(s, xs) / (np.dot(xs, xs) + 1e-12))
    return s - g * xs


def croma_audio(y):
    n_fft = 4096
    win = np.hanning(n_fft).astype(np.float32)
    nfr = 1 + (len(y) - n_fft) // HOP
    idx = np.arange(n_fft)[None, :] + HOP * np.arange(nfr)[:, None]
    S = np.abs(np.fft.rfft(y[idx] * win, axis=1)) ** 2
    f = np.fft.rfftfreq(n_fft, 1 / SR)
    sel = (f > 70) & (f < 1100)
    pc = np.mod(np.round(12 * np.log2(f[sel] / 440.0)) + 9, 12).astype(int)
    Ssel = S[:, sel]
    C = np.zeros((nfr, 12), np.float32)
    for k in range(12):
        C[:, k] = Ssel[:, pc == k].sum(1)
    en = C.sum(1)
    C = np.log1p(C / (np.percentile(en, 95) / 100 + 1e-12))
    db = 10 * np.log10(en + 1e-12)
    ref = np.percentile(db, 95)
    voz = 1 / (1 + np.exp(-(db - (ref - 22)) / 2.5))       # 0 = silêncio, 1 = voz
    C = C / (np.linalg.norm(C, axis=1, keepdims=True) + 1e-9)
    F = np.hstack([C * voz[:, None], (1 - voz)[:, None]])
    t = (np.arange(nfr) * HOP + n_fft / 2) / SR
    return F / (np.linalg.norm(F, axis=1, keepdims=True) + 1e-9), t


def linha_do_tempo(sistemas):
    """Tempo nominal (s) do início de cada compasso e duração, a partir de fórmulas e andamentos."""
    comp = {}
    form = [4, 4]
    seg_q = 60 / 100
    eventos_and = {}
    for s in sistemas:
        tx = s["textos"]
        for i, t in enumerate(tx):
            if t["t"] == "=" and 0 < i < len(tx) - 1 and tx[i + 1]["t"].isdigit():
                u, v = tx[i - 1]["t"], int(tx[i + 1]["t"])
                eventos_and[t["compasso"]] = {"q": 60 / v, "h": 30 / v, "q.": (60 / v) / 1.5}.get(u, 60 / v)
    t0 = 0.0
    for s in sistemas:
        for c in s["compassos"]:
            if "formula" in c:
                form = c["formula"]
            for k in range(c["qtd"]):
                n = c["n"] + k
                if n in eventos_and:
                    seg_q = eventos_and[n]
                quartos = form[0] * 4 / form[1]
                comp[n] = dict(t=t0, dur=quartos * seg_q, q=seg_q)
                t0 += quartos * seg_q
    return comp, t0


def posicoes(sistemas, comp):
    """Tempo nominal de cada nota e sílaba (fração no compasso medida a partir do 1º evento do segmento)."""
    notas, sil = [], []
    for si, s in enumerate(sistemas):
        for ci, c in enumerate(s["compassos"]):
            xs = [n["x"] for n in s["notas"] if n["compasso"] == c["n"]]
            x_ini = c["x0"]
            if ci == 0 and xs:
                x_ini = min(xs) - 4
            elif xs:
                x_ini = min(c["x0"] + 3, min(xs) - 2)
            larg = max(c["x1"] - x_ini, 1)
            base = comp[c["n"]]
            tot = base["dur"] * c["qtd"]
            mine = [n for n in s["notas"] if n["compasso"] == c["n"]]
            for n in mine:
                fr = min(max((n["x"] - x_ini) / larg, 0), 0.999)
                notas.append(dict(n, tn=base["t"] + fr * tot, q=base["q"], sis=si))
            for x in s["silabas"]:
                if x["compasso"] != c["n"]:
                    continue
                cx = x["x"] + min(4.0, (x["x1"] - x["x"]) / 2)
                near = [n for n in mine if n["pauta"] == x["pauta"]] or mine
                if near:
                    nb = min(near, key=lambda n: abs(n["x"] + 3 - cx))
                    if abs(nb["x"] + 3 - cx) < 10:
                        cx = nb["x"]
                        x = dict(x, tipo=nb["tipo"])
                fr = min(max((cx - x_ini) / larg, 0), 0.999)
                sil.append(dict(x, tn=base["t"] + fr * tot, sis=si))
    return notas, sil


def croma_partitura(notas, t_fim):
    nfr = int(t_fim * FPS) + 2
    C = np.zeros((nfr, 12), np.float32)
    por_pauta = {}
    for n in notas:
        por_pauta.setdefault((n["sis"], n["pauta"]), []).append(n)
    for k, ns in por_pauta.items():
        ons = np.array(sorted(set(round(n["tn"], 3) for n in ns)))
        for n in ns:
            prox = ons[ons > n["tn"] + 0.02]
            fim = min(prox[0] if len(prox) else n["tn"] + 4 * n["q"], n["tn"] + DUR_TIPO[n["tipo"]] * n["q"] * 1.05)
            a = int(n["tn"] * FPS)
            b = max(int(fim * FPS), a + 1)
            C[a:b, n["midi"] % 12] += 1
    voz = (C.sum(1) > 0).astype(np.float32)
    C = C / (np.linalg.norm(C, axis=1, keepdims=True) + 1e-9)
    F = np.hstack([C, (1 - voz)[:, None]])
    return F / (np.linalg.norm(F, axis=1, keepdims=True) + 1e-9)


@njit(cache=True)
def dtw(D, pen):
    n, m = D.shape
    A = np.full((n, m), np.inf)
    P = np.zeros((n, m), np.int8)
    A[0, 0] = D[0, 0]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            best = np.inf
            arg = 0
            if i > 0 and j > 0:
                v = A[i - 1, j - 1] + D[i, j]
                if v < best:
                    best = v
                    arg = 1
            if i > 0:
                v = A[i - 1, j] + D[i, j] + pen
                if v < best:
                    best = v
                    arg = 2
            if j > 0:
                v = A[i, j - 1] + D[i, j] + pen
                if v < best:
                    best = v
                    arg = 3
            A[i, j] = best
            P[i, j] = arg
    return A, P


def caminho(P, i, j):
    path = [(i, j)]
    while i > 0 or j > 0:
        a = P[i, j]
        if a == 1:
            i, j = i - 1, j - 1
        elif a == 2:
            i -= 1
        else:
            j -= 1
        path.append((i, j))
    return path[::-1]


def processa(m, score, dcant, dpb):
    sist = score[str(m)]
    comp, t_fim = linha_do_tempo(sist)
    notas, sil = posicoes(sist, comp)
    Fs = croma_partitura(notas, t_fim)
    y = residuo(m, dcant, dpb)
    Fa, ta = croma_audio(y)
    c_ent, t_ent = ENTRADA[m]
    s0 = comp[c_ent]["t"]
    i0 = max(int(s0 * FPS) - FPS, 0)
    j0 = int(np.searchsorted(ta, t_ent - 1.0))
    ult = max(n["tn"] for n in notas) + 3.0
    i1 = min(int(ult * FPS), len(Fs))
    D = (1 - Fs[i0:i1] @ Fa[j0:].T).astype(np.float64)
    A, P = dtw(D, 0.1)
    custo = A[-1] / (np.arange(A.shape[1]) + A.shape[0])
    j_fim = int(np.argmin(custo))
    path = caminho(P, A.shape[0] - 1, j_fim)
    pi = np.array([p[0] for p in path]) + i0
    pj = np.array([p[1] for p in path]) + j0
    tn_path = pi / FPS
    tc_path = ta[np.clip(pj, 0, len(ta) - 1)]
    tn_u, idx = np.unique(tn_path, return_index=True)
    # para cada tempo nominal, usa o meio do trecho horizontal do caminho
    tc_mid = np.array([np.mean(tc_path[tn_path == v]) for v in tn_u])
    tc_u = np.maximum.accumulate(tc_mid)

    def mapa(tn):
        return float(np.interp(tn, tn_u, tc_u))
    for x in sil:
        x["t_cant"] = round(mapa(x["tn"]), 3)
        x["t_pb"] = round(x["t_cant"] + OFFSET[m], 3)
    comps = {n: dict(t_cant=round(mapa(c["t"]), 3), t_pb=round(mapa(c["t"]) + OFFSET[m], 3), tn=round(c["t"], 3), q=round(c["q"], 4), dur_n=round(c["dur"], 4))
             for n, c in comp.items() if c["t"] >= s0 - 0.5}
    custo_med = float(np.mean([D[p[0], p[1]] for p in path]))
    return dict(silabas=sil, compassos=comps, custo_medio=round(custo_med, 3), fim_cant=round(float(tc_u[-1]), 2),
                caminho=[[round(float(a), 2), round(float(b), 2)] for a, b in zip(tn_u[::4], tc_u[::4])])


if __name__ == "__main__":
    score = json.load(open(sys.argv[1]))
    so = [int(a) for a in sys.argv[5:]] or list(range(1, 7))
    res = {}
    for m in so:
        r = processa(m, score, sys.argv[2], sys.argv[3])
        res[m] = r
        print(m, "custo", r["custo_medio"], "fim", r["fim_cant"], "silabas", len(r["silabas"]), flush=True)
    json.dump(res, open(sys.argv[4], "w"), ensure_ascii=False, default=float)
