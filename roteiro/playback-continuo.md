# Playback contínuo da cantata

Faixa única com os seis playbacks, montada em 15/11/2026 com `scripts/montar_continuo.py`. Duração: 24:57.8.

Cada playback entra no mesmo ponto em que a música começa na gravação original contínua (`00_cantata-completa_cantada-EN`). Por isso o intervalo entre uma música e a seguinte fica como no original, em vez dos 7 a 8 s de silêncio que cada playback traz no fim.

| Faixa | Início na faixa única | Pausa até a próxima (último som → primeiro som) |
|---|---|---|
| 1 O Amor desceu | 0:00.0 | 1,2 s |
| 2 Vem, Emanuel, vem | 4:17.6 | 1,2 s |
| 3 Dá-nos paz | 8:58.8 | 1,9 s |
| 4 Ouça a alegre canção | 13:12.0 | 1,8 s |
| 5 O Amor seja seu e meu | 17:23.9 | 2,9 s |
| 6 Amor divino | 21:48.3 | — |

Os segundos exatos estão em `playback-continuo.json` (`inicio_s`).

**Volume.** O equilíbrio entre as músicas foi mantido como os playbacks foram entregues ("Dá-nos paz" mais baixa, o final mais forte). Só foi aplicado um ganho geral para o pico ficar em −1,5 dBFS (loudness integrada: −22,1 LUFS). Copiar o volume de cada música da gravação cantada não deu resultado confiável, porque ela tem outra masterização.

**Legendas.** As legendas por faixa continuam valendo; para a faixa única, somar o início da faixa da tabela acima. A legenda pronta para a faixa única e o vídeo com o playback e a letra estão no Drive do projeto, fora deste repositório (contêm a letra).

Esta montagem adota a pausa curta da gravação original (decisão 2 da Etapa 1). Se o regente quiser outra pausa, o script remonta a faixa.
