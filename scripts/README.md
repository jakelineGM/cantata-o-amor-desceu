# Scripts

Scripts usados nas Etapas 1 e 2. Rodam em Python 3 com `numpy`, `scipy`, `numba`, `pymupdf`, `pyspellchecker` e o `ffmpeg` instalado. Rode com `python3 -I`.

Nenhum arquivo de mídia, partitura ou texto de letra fica no repositório. Os caminhos de entrada são passados na linha de comando.

## Ordem

| # | Script | Entrada | Saída |
|---|---|---|---|
| 1 | `medir_pb56.py` | pasta dos playbacks 5 e 6, pasta das faixas cantadas | identificação, defasagem e limites de cada playback (Etapa 1) |
| 2 | `extrair_v4.py` | partitura vocal em português (PDF vetorial do Sibelius) | geometria: pautas, barras e caracteres visíveis (ignora o que foi coberto de branco) |
| 3 | `interpretar_v4.py` | saída do 2 | compassos numerados, notas (altura MIDI), sílabas da letra, fórmulas e andamentos |
| 4 | `alinhar.py` | saída do 3, faixas cantadas, playbacks | tempo de cada sílaba e de cada compasso (DTW de croma contra a voz isolada) |
| 5 | `narracao.py` | JSON com o texto da narração por trecho (fora do repositório) | legendas provisórias da narração |
| 6 | `etapa2.py` | saídas do 3 e do 4, `roteiro/mapa-de-tempos.json`, saída do 5 | legendas `.srt` por faixa, da cantata inteira e de conferência; `etapa2.json` |
| 7 | `doc_etapa2.py` | `etapa2.json` | `etapa-2-letras.md`; com `SEM_LETRA=1`, a versão pública sem o texto |
| 8 | `conferir_tempos.py` | `etapa2.json`, faixas cantadas, playbacks | compara o início de cada verso com a entrada da voz |
| 9 | `montar_continuo.py` | playbacks, faixas cantadas, posições das faixas na gravação contínua | faixa única de playback e `playback-continuo.json` |

## Exemplo

```
python3 -I scripts/extrair_v4.py partitura_v4.pdf out/v4_geo.json
python3 -I scripts/interpretar_v4.py out/v4_geo.json out/v4_score.json
python3 -I scripts/alinhar.py out/v4_score.json cantadas/ playbacks/ out/alinhamento.json
python3 -I scripts/narracao.py narracao_trechos.json out/narracao.json
python3 -I scripts/etapa2.py out/v4_score.json out/alinhamento.json roteiro/mapa-de-tempos.json saida/ out/narracao.json
SEM_LETRA=1 python3 -I scripts/doc_etapa2.py saida/etapa2.json roteiro/etapa-2-letras.md
```

Os nomes dos arquivos de áudio esperados estão no topo de `alinhar.py` e `montar_continuo.py`.
