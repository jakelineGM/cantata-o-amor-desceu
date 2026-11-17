"""Junta os seis playbacks numa faixa única, na mesma posição em que cada música está na gravação original contínua
(00_cantata-completa_cantada-EN.m4a), com o mesmo equilíbrio de volume entre as faixas.
Uso: python3 -I montar_continuo.py <pasta_playbacks> <pasta_cantadas> <completa.json> <pasta_saida>
Saída: playback_cantata-completa.wav e posicoes.json (início de cada playback na faixa única, s)."""
import json, subprocess, sys
import numpy as np

SR = 44100
PB = {1: "01_o-amor-desceu_playback.mp3", 2: "02_vem-emanuel-vem_playback.mp3", 3: "03_da-nos-paz_playback.mp3",
      4: "04_ouca-a-alegre-cancao_playback.mp3", 5: "05_o-amor-seja-seu-e-meu_playback.mp3", 6: "06_amor-divino_playback.mp3"}
CANT = {1: "01_o_amor_desceu_cantado.mpeg", 2: "02_vem_emanuel_cantada.mpeg", 3: "03_da_nos_paz_cantado.mpeg",
        4: "04_ouca_a_alegre_cancao_cantado.mpeg", 5: "05_o_amor_seja_seu_e_meu_cantada.mpeg", 6: "06_amor_divino_cantada.mpeg"}
OFFSET = {1: 0.228, 2: 0.427, 3: 0.429, 4: 0.435, 5: 0.4306, 6: 0.4399}   # tempo no playback = tempo na cantada + offset


def load(path, ch):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", str(ch), "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, dtype=np.float32)
    return x.reshape(-1, ch).copy() if ch > 1 else x.copy()


def ganho(n, dpb, dcant):
    """Fator que leva o playback ao nível do acompanhamento dentro da faixa cantada (mesmo método do resíduo)."""
    s = load(f"{dcant}/{CANT[n]}", 1)
    x = load(f"{dpb}/{PB[n]}", 1)
    off = int(round(OFFSET[n] * SR))
    xs = np.zeros_like(s)
    seg = x[off: off + len(s)]
    xs[: len(seg)] = seg
    return float(np.dot(s, xs) / (np.dot(xs, xs) + 1e-12))


if __name__ == "__main__":
    dpb, dcant, fcomp, out = sys.argv[1:5]
    comp = {c["faixa"]: c["inicio"] for c in json.load(open(fcomp))}
    pos = {n: comp[n] - OFFSET[n] for n in PB}          # onde o arquivo de playback começa na linha do tempo original
    desloc = -min(pos.values())                          # a faixa única começa no início do 1º playback
    pos = {n: p + desloc for n, p in pos.items()}
    faixas, gs = {}, {}
    for n in PB:
        faixas[n] = load(f"{dpb}/{PB[n]}", 2)
        gs[n] = 1.0   # mantém o equilíbrio entre faixas como os playbacks foram entregues
    fim = max(pos[n] + len(faixas[n]) / SR for n in PB)
    buf = np.zeros((int(np.ceil(fim * SR)) + 1, 2), np.float32)
    for n in PB:
        a = int(round(pos[n] * SR))
        buf[a: a + len(faixas[n])] += gs[n] * faixas[n]
    pico = float(np.max(np.abs(buf)))
    alvo = 10 ** (-1.5 / 20)                            # pico final em −1,5 dBFS (margem para pico real)
    buf *= alvo / pico
    pcm = (np.clip(buf, -1, 1) * 32767).astype("<i2")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "s16le", "-ar", str(SR), "-ac", "2", "-i", "-",
                    f"{out}/playback_cantata-completa.wav"], input=pcm.tobytes(), check=True)
    info = dict(inicio_s={n: round(pos[n], 3) for n in PB}, ganho_relativo={n: round(gs[n], 3) for n in PB},
                ganho_global=round(alvo / pico, 4), duracao_s=round(len(buf) / SR, 3))
    json.dump(info, open(f"{out}/posicoes.json", "w"), indent=1)
    print(json.dumps(info, indent=1))
