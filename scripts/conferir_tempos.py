"""Confere o início de cada legenda com a subida de energia da voz isolada (cantada − playback).
Uso: python3 -I conferir_tempos.py <etapa2.json> <pasta_cantadas> <pasta_playbacks>"""
import json, sys, importlib.util
import numpy as np
spec = importlib.util.spec_from_file_location("al", __import__("os").path.join(__import__("os").path.dirname(__file__), "alinhar.py"))
al = importlib.util.module_from_spec(spec); spec.loader.exec_module(al)
e2 = json.load(open(sys.argv[1]))
for m in range(1, 7):
    y = al.residuo(m, sys.argv[2], sys.argv[3])
    hop = 441
    n = len(y) // hop
    db = 10 * np.log10(np.mean(y[: n * hop].reshape(n, hop) ** 2, axis=1) + 1e-10)
    db = np.convolve(db, np.ones(5) / 5, mode="same")
    der = np.gradient(db)
    off = al.OFFSET[m]
    gs = e2[str(m)]["grupos"]
    devs = []
    for i, g in enumerate(gs):
        if i and g["ini"] - gs[i - 1]["fim"] < 0.6:
            continue
        t = g["ini"] - off
        k0, k1 = int((t - 1.0) * 50), int((t + 1.0) * 50)
        if k0 < 0 or k1 >= n:
            continue
        k = k0 + int(np.argmax(der[k0:k1]))
        devs.append(k / 50 - t)
    d = np.array(devs)
    print(m, "inícios testados", len(d), "mediana", round(float(np.median(d)), 2), "≤0,3 s:", round(float(np.mean(abs(d) <= 0.3)), 2),
          "≤0,6 s:", round(float(np.mean(abs(d) <= 0.6)), 2), "piores", sorted(np.round(d, 2), key=abs)[-3:])
