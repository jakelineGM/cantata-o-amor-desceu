"""Mede os playbacks 5 e 6: identificação, defasagem, deriva, limites, picos e resíduo de voz.
Uso: python3 -I medir_pb56.py <pasta_playbacks> <pasta_cantadas> <saida.json>"""
import json, subprocess, sys
import numpy as np
from scipy.signal import fftconvolve

SR = 22050
HOP = 441  # 20 ms


def load(path, sr=SR, stereo=False):
    ch = 2 if stereo else 1
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", str(ch), "-ar", str(sr),
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, dtype=np.float32)
    return x.reshape(-1, 2) if stereo else x


def frames_db(x):
    n = len(x) // HOP
    r = np.sqrt(np.mean(x[: n * HOP].reshape(n, HOP) ** 2, axis=1) + 1e-20)
    return 20 * np.log10(r)


def bounds(x, thr):
    db = frames_db(x)
    idx = np.where(db > thr)[0]
    return idx[0] * HOP / SR, (idx[-1] + 1) * HOP / SR


def xcorr_peak(a, b):
    """Retorna (lag em amostras, pico normalizado) tal que a[t] ~ b[t - lag]."""
    a = (a - a.mean()) / (a.std() + 1e-12)
    b = (b - b.mean()) / (b.std() + 1e-12)
    c = fftconvolve(a, b[::-1], mode="full") / min(len(a), len(b))
    k = int(np.argmax(c))
    return k - (len(b) - 1), float(c[k])


def env(x, sr, hop):
    n = len(x) // hop
    return np.sqrt(np.mean(x[: n * hop].reshape(n, hop) ** 2, axis=1))


pb_dir, sung_dir, out = sys.argv[1:4]
pbs = {5: f"{pb_dir}/5.mp3", 6: f"{pb_dir}/6.mp3"}
sung = {
    1: "01_o_amor_desceu_cantado.mpeg", 2: "02_vem_emanuel_cantada.mpeg",
    3: "03_da_nos_paz_cantado.mpeg", 4: "04_ouca_a_alegre_cancao_cantado.mpeg",
    5: "05_o_amor_seja_seu_e_meu_cantada.mpeg", 6: "06_amor_divino_cantada.mpeg",
}
S = {k: load(f"{sung_dir}/{v}") for k, v in sung.items()}
res = {}
for n, p in pbs.items():
    x = load(p)
    st = load(p, stereo=True)
    info = {"arquivo": p.split("/")[-1], "n_amostras": len(x)}
    ex = env(x, SR, 220)
    corr = {}
    for k, s in S.items():
        lag, pk = xcorr_peak(env(s, SR, 220), ex)
        corr[k] = round(pk, 3)
    info["correlacao_envelope"] = corr
    best = max(corr, key=corr.get)
    info["faixa_identificada"] = best
    s = S[best]
    lag, pk = xcorr_peak(s, x)  # s[t] ~ x[t - lag]  => playback = cantada + (-lag)
    info["offset_s"] = round(-lag / SR, 4)
    info["pico_amostra"] = round(pk, 3)
    off = -lag
    dr = []
    for t0 in np.arange(20, len(s) / SR - 40, 40):
        a = s[int(t0 * SR): int((t0 + 30) * SR)]
        b0 = int((t0 + off / SR - 1) * SR)
        b = x[max(b0, 0): b0 + int(32 * SR)]
        l2, p2 = xcorr_peak(b, a)
        dr.append([round(float(t0), 1), round((l2 + max(b0, 0) - int(t0 * SR)) / SR, 4), round(p2, 3)])
    info["deriva"] = dr
    for thr in (-50, -60):
        f, l = bounds(x, thr)
        info[f"primeiro{abs(thr)}"] = round(f, 2)
        info[f"ultimo{abs(thr)}"] = round(l, 2)
    info["dur_decod"] = round(len(x) / SR, 3)
    info["pico_dbfs"] = round(20 * np.log10(np.max(np.abs(st)) + 1e-12), 1)
    xs = np.zeros_like(s)
    if off >= 0:
        seg = x[off: off + len(s)]
    else:
        seg = np.concatenate([np.zeros(-off, dtype=np.float32), x[: len(s) + off]])
    xs[: len(seg)] = seg[: len(s)]
    g = float(np.dot(s, xs) / (np.dot(xs, xs) + 1e-12))
    r = s - g * xs
    info["ganho"] = round(g, 3)
    info["residuo_db_20ms"] = [round(float(v), 1) for v in frames_db(r)]
    info["cantada_db_20ms"] = [round(float(v), 1) for v in frames_db(s)]
    info["rel_residuo_total_db"] = round(10 * np.log10(np.sum(r ** 2) / np.sum(s ** 2)), 1)
    res[n] = info
    print(n, {k: v for k, v in info.items() if not k.endswith("20ms")})
json.dump(res, open(out, "w"), indent=1, default=float)
