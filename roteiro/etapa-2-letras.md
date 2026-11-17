# Cantata "O Amor desceu" — Etapa 2: Letras alinhadas

Situação: entregue para aprovação em 14/11/2026, adiantada antes da aprovação formal da Etapa 1. Base: partitura do grupo `partitura-grupo_o-amor-desceu_PT_v4_definitiva.pdf` e gravação cantada de referência.

**Versão pública, sem a letra.** Este repositório é público e a letra em português é tradução de obra com direitos da Lorenz; por isso aqui ficam só compassos, vozes e tempos. A versão com a letra, as legendas .srt e os vídeos de conferência estão no Drive do projeto (pasta `roteiro` e `legendas`). Os scripts em `scripts/` regeram tudo a partir da partitura e dos áudios.

## Como ler

- Cada linha da tabela é um verso como aparece na legenda. Quando vozes cantam textos diferentes ao mesmo tempo, a legenda mostra duas ou três linhas.
- **Vozes:** S/C = sopranos e contraltos (pauta de cima), T/B = tenores e baixos, Desc. = descante, todos = mesmo texto nas duas pautas.
- **Início e fim:** tempo dentro do arquivo de playback da faixa (m:ss.s), do primeiro ataque à última nota do verso. Na legenda, cada verso aparece 0,25 s antes e fica até 0,4 s depois.
- **Compassos:** numeração da partitura do grupo, igual à da partitura original Lorenz (as seis músicas têm o mesmo número de compassos, conforme a revisão).

## Letra original em inglês

A tabela não traz a coluna com a letra em inglês. A letra original é de 2014, com direitos da Lorenz, e não a transcrevo. Para conferir verso a verso, use a coluna **Compassos** com a partitura original licenciada, ou a legenda de conferência, que traz compassos e vozes ao lado do português. Os cânticos tradicionais citados em cada música estão listados pelo título.

## Como os tempos foram gerados

1. Letra, notas e compassos foram lidos direto do PDF vetorial da v4. O texto apagado por camada branca nas correções foi descartado.
2. A voz foi isolada da gravação cantada subtraindo o playback alinhado.
3. A partitura foi alinhada à voz isolada por comparação de alturas (croma) ao longo do tempo, a partir da entrada do coro de cada música. O mapa compasso a compasso foi suavizado para eliminar barras deslocadas.
4. Conferência: nas músicas 1, 3, 5 e 6, o início dos versos bate com a subida de energia da voz, com mediana entre −0,07 e 0 s. Nas músicas 2 e 4 a voz isolada tem mais resto de acompanhamento e a conferência automática é menos conclusiva; onde há subida nítida, o erro fica até 0,2 s.
5. A gravação de referência é em inglês. Como o português segue as mesmas notas, o tempo de cada sílaba vem da posição da nota na partitura. Onde o grupo dividiu uma nota para caber sílabas, o tempo da sílaba extra é estimado pela posição na pauta.

## Métrica e prosódia

A v4 já traz cada sílaba em português sob uma nota, então não há sílaba sobrando. O que foi verificado:

- **Acento:** palavras com a sílaba tônica em tempo fraco enquanto uma sílaba átona (que não seja acento secundário) cai na cabeça do compasso. Aparecem na coluna Observação.
- **Ritmo alterado para caber o português:** segundo a auditoria da v3, 46 compassos-pauta dividem uma nota do original em duas para caber as sílabas, além das adaptações D2 (M2 c. 124 e c. 180) e D3 (M5 c. 26). A auditoria não lista os 46 compassos; para sinalizá-los verso a verso é preciso essa lista.
- **Elisões** (duas vogais numa nota, marcadas com _ na partitura): contadas por música. São normais no canto em português e não foram tratadas como problema.

## 1. O Amor desceu (Abertura) — Love Came Down (Opener)

Cânticos tradicionais citados (asterisco na partitura): Silent Night! Holy Night! (c. 1); Love Divine, All Loves Excelling (c. 30); Angels We Have Heard on High (c. 34); On Christmas Night All Christians Sing (c. 40); He Is Born, the Divine Christ Child (c. 60); O Come, All Ye Faithful (c. 62); Once in Royal David's City (c. 81); Hark! the Herald Angels Sing (c. 94).

**Narração 1 (tempo provisório).** Voz M = narrador, F = narradora.

| # | Compasso | Voz | Início | Fim |
|---|---|---|---|---|
| N1 | 2 | M | 0:03.0 | 0:09.0 |
| N2 | 5 | F | 0:10.0 | 0:13.2 |
| N3 | 5 | F | 0:13.2 | 0:17.0 |
| N4 | 10 | M | 0:22.0 | 0:28.0 |
| N5 | 18 | F | 0:38.0 | 0:41.1 |
| N6 | 18 | F | 0:41.1 | 0:46.0 |

**Letra cantada.**

| # | Compassos | Vozes | Linhas | Início | Fim | Observação |
|---|---|---|---|---|---|---|
| 1 | 22–25 | todos | 1 | 0:47.1 | 0:54.8 |  |
| 2 | 25–30 | todos<br>S/C | 2 | 0:53.3 | 1:04.7 |  |
| 3 | 30–31 | T/B | 1 | 1:03.6 | 1:07.8 |  |
| 4 | 31–37 | S/C<br>T/B<br>T/B | 3 | 1:07.7 | 1:20.1 | três textos simultâneos |
| 5 | 37–39 | S/C<br>T/B | 2 | 1:18.1 | 1:24.2 |  |
| 6 | 40–42 | S/C | 1 | 1:25.6 | 1:29.8 |  |
| 7 | 42–44 | S/C | 1 | 1:30.0 | 1:33.8 |  |
| 8 | 44–46 | S/C | 1 | 1:34.1 | 1:38.0 |  |
| 9 | 46–48 | S/C | 1 | 1:38.2 | 1:42.1 |  |
| 10 | 49–51 | S/C<br>T/B | 2 | 1:42.7 | 1:49.3 |  |
| 11 | 52–55 | S/C | 1 | 1:49.9 | 1:57.2 |  |
| 12 | 57–60 | S/C<br>T/B | 2 | 1:59.4 | 2:07.0 |  |
| 13 | 60–64 | S/C<br>S/C<br>T/B | 3 | 2:06.9 | 2:15.7 | três textos simultâneos |
| 14 | 64–67 | S/C<br>T/B | 2 | 2:15.2 | 2:22.4 |  |
| 15 | 69–72 | todos | 1 | 2:24.2 | 2:32.1 |  |
| 16 | 72–76 | todos | 1 | 2:32.2 | 2:40.5 |  |
| 17 | 76–79 | todos | 1 | 2:40.7 | 2:47.7 |  |
| 18 | 80–81 | S/C<br>T/B | 2 | 2:47.7 | 2:50.3 |  |
| 19 | 81–84 | S/C | 1 | 2:49.8 | 2:57.8 |  |
| 20 | 85–88 | T/B | 1 | 2:58.2 | 3:06.3 |  |
| 21 | 89–93 | S/C | 1 | 3:06.6 | 3:17.3 |  |
| 22 | 94–96 | S/C | 1 | 3:19.3 | 3:23.8 |  |
| 23 | 96–100 | S/C | 1 | 3:24.2 | 3:34.0 |  |
| 24 | 102–103 | S/C | 1 | 3:36.2 | 3:40.1 |  |
| 25 | 103–107 | S/C<br>T/B | 2 | 3:39.6 | 3:48.5 |  |
| 26 | 111–113 | S/C | 1 | 3:56.8 | 4:08.9 |  |

Elisões nesta música: 23. Sinalizações de acento: 0.

## 2. Vem, Emanuel, vem — Come, Emmanuel, Come (Hope)

Cânticos tradicionais citados (asterisco na partitura): Lo, How a Rose E'er Blooming (c. 7); On This Day Earth Shall Ring (c. 1); O Come, O Come, Emmanuel (c. 71); Come, Thou Long Expected Jesus (c. 122).

**Narração 2 (tempo provisório).** Voz M = narrador, F = narradora.

| # | Compasso | Voz | Início | Fim |
|---|---|---|---|---|
| N1 | 2 | M | 0:08.0 | 0:14.1 |
| N2 | 5 | M | 0:14.1 | 0:19.0 |
| N3 | 8 | F | 0:23.0 | 0:27.4 |
| N4 | 8 | F | 0:27.4 | 0:32.0 |

**Letra cantada.**

| # | Compassos | Vozes | Linhas | Início | Fim | Observação |
|---|---|---|---|---|---|---|
| 1 | 29–33 | S/C | 1 | 1:00.6 | 1:05.4 |  |
| 2 | 33–36 | S/C | 1 | 1:05.7 | 1:09.1 |  |
| 3 | 37–41 | S/C | 1 | 1:10.5 | 1:15.8 |  |
| 4 | 41–44 | S/C | 1 | 1:15.6 | 1:19.0 |  |
| 5 | 46–49 | S/C | 1 | 1:20.7 | 1:25.3 |  |
| 6 | 50–52 | S/C | 1 | 1:25.7 | 1:29.0 |  |
| 7 | 53–57 | S/C | 1 | 1:30.6 | 1:35.2 |  |
| 8 | 57–60 | S/C | 1 | 1:35.5 | 1:39.0 |  |
| 9 | 62–68 | S/C | 1 | 1:40.6 | 1:48.8 |  |
| 10 | 71–76 | T/B | 1 | 1:52.5 | 1:58.8 |  |
| 11 | 76–79 | S/C<br>T/B | 2 | 1:58.2 | 2:03.0 |  |
| 12 | 79–84 | T/B | 1 | 2:02.5 | 2:08.7 |  |
| 13 | 84–85 | S/C | 1 | 2:08.2 | 2:10.8 |  |
| 14 | 87–92 | S/C | 1 | 2:12.4 | 2:18.7 |  |
| 15 | 93–98 | S/C | 1 | 2:19.8 | 2:26.1 |  |
| 16 | 99–100 | S/C | 1 | 2:27.4 | 2:28.7 |  |
| 17 | 101–102 | S/C | 1 | 2:29.9 | 2:31.2 |  |
| 18 | 103–106 | S/C | 1 | 2:32.3 | 2:36.1 |  |
| 19 | 107–114 | todos | 1 | 2:37.3 | 2:46.2 |  |
| 20 | 114–117 | S/C<br>T/B | 2 | 2:46.0 | 2:50.0 |  |
| 21 | 118–119 | S/C | 1 | 2:50.6 | 2:53.0 |  |
| 22 | 122–125 | S/C | 1 | 2:55.1 | 3:00.0 |  |
| 23 | 126–129 | S/C | 1 | 3:00.0 | 3:04.6 |  |
| 24 | 129–133 | S/C | 1 | 3:04.9 | 3:09.9 |  |
| 25 | 134–137 | S/C | 1 | 3:10.0 | 3:14.8 |  |
| 26 | 139–145 | S/C | 1 | 3:16.2 | 3:24.4 |  |
| 27 | 153–153 | S/C | 1 | 3:33.5 | 3:35.2 |  |
| 28 | 155–159 | S/C | 1 | 3:36.0 | 3:41.9 |  |
| 29 | 161–167 | S/C | 1 | 3:43.5 | 3:51.8 |  |
| 30 | 169–172 | S/C | 1 | 3:53.4 | 3:58.0 |  |
| 31 | 173–175 | S/C | 1 | 3:58.4 | 4:01.7 |  |
| 32 | 176–178 | S/C | 1 | 4:03.3 | 4:05.9 |  |
| 33 | 179–183 | S/C | 1 | 4:05.9 | 4:11.7 |  |
| 34 | 185–191 | S/C | 1 | 4:13.6 | 4:21.6 |  |
| 35 | 195–198 | S/C | 1 | 4:26.2 | 4:30.7 |  |
| 36 | 199–202 | S/C | 1 | 4:31.2 | 4:36.4 |  |

Elisões nesta música: 14. Sinalizações de acento: 0.

## 3. Dá-nos paz — Grant Us Peace (Peace)

Cânticos tradicionais citados (asterisco na partitura): Come, Thou Long Expected Jesus (c. 5); Lo! How a Rose E'er Blooming (c. 12); Away in a Manger (c. 44).

**Narração 3 (tempo provisório).** Voz M = narrador, F = narradora.

| # | Compasso | Voz | Início | Fim |
|---|---|---|---|---|
| N1 | 6 | F | 0:12.0 | 0:18.6 |
| N2 | 9 | M | 0:18.6 | 0:24.6 |
| N3 | 13 | M | 0:24.6 | 0:33.0 |

**Letra cantada.**

| # | Compassos | Vozes | Linhas | Início | Fim | Observação |
|---|---|---|---|---|---|---|
| 1 | 25–31 | S/C | 1 | 0:48.7 | 1:01.1 |  |
| 2 | 33–35 | S/C | 1 | 1:02.3 | 1:07.9 |  |
| 3 | 37–40 | S/C | 1 | 1:09.3 | 1:15.8 |  |
| 4 | 41–42 | T/B | 1 | 1:16.4 | 1:20.4 |  |
| 5 | 43–45 | S/C | 1 | 1:21.0 | 1:25.1 |  |
| 6 | 46–54 | S/C | 1 | 1:26.0 | 1:39.9 |  |
| 7 | 55–57 | S/C | 1 | 1:41.4 | 1:45.7 |  |
| 8 | 58–60 | S/C | 1 | 1:46.6 | 1:50.4 |  |
| 9 | 61–63 | S/C | 1 | 1:51.9 | 1:56.2 |  |
| 10 | 64–66 | S/C | 1 | 1:57.1 | 2:01.0 |  |
| 11 | 68–70 | S/C | 1 | 2:03.3 | 2:08.4 |  |
| 12 | 70–75 | S/C | 1 | 2:08.4 | 2:16.6 |  |
| 13 | 75–79 | T/B | 1 | 2:17.0 | 2:23.6 |  |
| 14 | 79–82 | S/C | 1 | 2:24.1 | 2:30.1 |  |
| 15 | 86–92 | S/C | 1 | 2:35.0 | 2:47.8 |  |
| 16 | 94–96 | S/C | 1 | 2:48.8 | 2:54.5 |  |
| 17 | 98–101 | S/C | 1 | 2:55.8 | 3:02.6 |  |
| 18 | 107–115 | S/C<br>T/B<br>T/B | 3 | 3:13.3 | 3:27.7 | três textos simultâneos |
| 19 | 115–119 | S/C<br>T/B | 2 | 3:28.2 | 3:35.9 |  |
| 20 | 119–123 | S/C<br>T/B | 2 | 3:35.7 | 3:43.4 |  |
| 21 | 127–130 | S/C | 1 | 3:49.5 | 3:57.0 |  |
| 22 | 134–134 | S/C | 1 | 4:03.4 | 4:05.8 |  |

Elisões nesta música: 7. Sinalizações de acento: 0.

## 4. Ouça a alegre canção — Listen to the Joyful Song (Joy)

Cânticos tradicionais citados (asterisco na partitura): He Is Born, the Divine Christ Child (c. 1); Joy to the World! the Lord Is Come (c. 1); Hark! the Herald Angels Sing (c. 70); God Rest Ye Merry, Gentlemen (c. 94).

**Narração 4 (tempo provisório).** Voz M = narrador, F = narradora.

| # | Compasso | Voz | Início | Fim |
|---|---|---|---|---|
| N1 | 3 | M | 0:11.0 | 0:15.7 |
| N2 | 5 | M | 0:15.7 | 0:20.1 |
| N3 | 5 | F | 0:20.1 | 0:23.5 |
| N4 | 9 | F | 0:23.5 | 0:26.0 |
| N5 | 9 | M | 0:27.0 | 0:32.0 |
| N6 | 12 | F | 0:32.0 | 0:35.2 |
| N7 | 12 | F | 0:35.2 | 0:38.0 |

**Letra cantada.**

| # | Compassos | Vozes | Linhas | Início | Fim | Observação |
|---|---|---|---|---|---|---|
| 1 | 24–25 | S/C | 1 | 0:51.3 | 0:54.4 |  |
| 2 | 26–27 | S/C | 1 | 0:54.3 | 0:57.1 |  |
| 3 | 28–29 | S/C | 1 | 0:57.3 | 1:00.4 | acento: "U-na-se" (c. 28), tônica "na" em tempo fraco e "U" na cabeça do compasso |
| 4 | 29–31 | S/C | 1 | 1:00.2 | 1:03.1 |  |
| 5 | 32–33 | S/C | 1 | 1:03.2 | 1:06.3 |  |
| 6 | 33–35 | S/C | 1 | 1:06.1 | 1:09.0 |  |
| 7 | 36–37 | S/C | 1 | 1:09.2 | 1:12.0 |  |
| 8 | 38–40 | S/C | 1 | 1:12.2 | 1:16.7 |  |
| 9 | 42–44 | S/C | 1 | 1:18.0 | 1:22.6 |  |
| 10 | 46–48 | S/C | 1 | 1:24.2 | 1:28.6 |  |
| 11 | 50–53 | S/C | 1 | 1:30.0 | 1:35.4 |  |
| 12 | 54–57 | S/C | 1 | 1:36.1 | 1:41.3 | acento: "pro-cla-man-do" (c. 55), tônica "man" em tempo fraco e "do" na cabeça do compasso |
| 13 | 58–59 | S/C | 1 | 1:42.0 | 1:45.1 |  |
| 14 | 60–61 | S/C | 1 | 1:45.0 | 1:47.7 |  |
| 15 | 61–63 | S/C | 1 | 1:47.9 | 1:50.8 |  |
| 16 | 64–66 | S/C | 1 | 1:51.0 | 1:55.5 |  |
| 17 | 70–72 | S/C | 1 | 2:00.0 | 2:03.7 |  |
| 18 | 72–73 | S/C | 1 | 2:03.2 | 2:05.7 |  |
| 19 | 74–75 | T/B | 1 | 2:05.9 | 2:08.6 |  |
| 20 | 76–77 | T/B | 1 | 2:08.8 | 2:11.6 |  |
| 21 | 77–79 | S/C | 1 | 2:11.7 | 2:14.5 |  |
| 22 | 80–81 | T/B | 1 | 2:14.7 | 2:17.5 |  |
| 23 | 81–83 | S/C | 1 | 2:17.7 | 2:20.6 |  |
| 24 | 84–85 | S/C | 1 | 2:20.8 | 2:23.5 |  |
| 25 | 86–87 | S/C | 1 | 2:23.8 | 2:26.5 |  |
| 26 | 88–91 | S/C | 1 | 2:26.8 | 2:32.7 |  |
| 27 | 93–94 | S/C | 1 | 2:34.1 | 2:37.2 |  |
| 28 | 94–96 | T/B | 1 | 2:36.7 | 2:39.5 |  |
| 29 | 96–99 | S/C<br>T/B | 2 | 2:39.3 | 2:44.5 |  |
| 30 | 99–104 | S/C<br>T/B | 2 | 2:44.1 | 2:51.8 |  |
| 31 | 104–106 | S/C | 1 | 2:51.7 | 2:55.0 |  |
| 32 | 107–109 | S/C | 1 | 2:56.1 | 2:59.5 |  |
| 33 | 110–112 | S/C | 1 | 3:00.2 | 3:04.4 |  |
| 34 | 113–115 | S/C<br>T/B<br>T/B | 3 | 3:04.5 | 3:08.5 | três textos simultâneos |
| 35 | 116–117 | S/C | 1 | 3:08.4 | 3:11.9 |  |
| 36 | 121–122 | S/C | 1 | 3:15.9 | 3:18.9 |  |
| 37 | 123–124 | S/C | 1 | 3:18.9 | 3:22.1 |  |
| 38 | 125–128 | Desc.<br>Desc.<br>S/C<br>S/C | 4 | 3:22.4 | 3:28.0 | três textos simultâneos |
| 39 | 128–130 | Desc.<br>S/C | 2 | 3:27.5 | 3:31.3 | acento: "U-na-se" (c. 129), tônica "na" em tempo fraco e "U" na cabeça do compasso |
| 40 | 131–132 | Desc. + S/C | 1 | 3:31.2 | 3:34.0 |  |
| 41 | 133–136 | Desc.<br>S/C<br>S/C | 3 | 3:34.1 | 3:40.0 | três textos simultâneos |
| 42 | 137–137 | S/C | 1 | 3:40.2 | 3:42.2 |  |
| 43 | 138–141 | todos<br>S/C | 2 | 3:42.9 | 3:49.5 |  |
| 44 | 144–147 | S/C | 1 | 3:52.7 | 3:59.0 |  |
| 45 | 150–152 | S/C | 1 | 4:02.3 | 4:07.3 |  |

Elisões nesta música: 31. Sinalizações de acento: 3.

## 5. O Amor seja seu e meu — Love Be Yours, Love Be Mine (Love)

Cânticos tradicionais citados (asterisco na partitura): The First Noel (c. 1); Love Came Down at Christmas (c. 13); Gesù Bambino (c. 33).

**Narração 5 (tempo provisório).** Voz M = narrador, F = narradora.

| # | Compasso | Voz | Início | Fim |
|---|---|---|---|---|
| N1 | 2 | F | 0:05.0 | 0:12.9 |
| N2 | 6 | F | 0:12.9 | 0:17.5 |
| N3 | 6 | F | 0:17.5 | 0:24.0 |
| N4 | 6 | M | 0:25.0 | 0:29.3 |
| N5 | 10 | F | 0:29.3 | 0:32.1 |
| N6 | 10 | M | 0:32.1 | 0:35.0 |

**Letra cantada.**

| # | Compassos | Vozes | Linhas | Início | Fim | Observação |
|---|---|---|---|---|---|---|
| 1 | 13–14 | S/C | 1 | 0:37.2 | 0:43.2 |  |
| 2 | 15–16 | S/C | 1 | 0:43.6 | 0:49.0 |  |
| 3 | 17–18 | S/C | 1 | 0:50.5 | 0:57.1 |  |
| 4 | 19–20 | S/C | 1 | 0:57.6 | 1:02.2 |  |
| 5 | 21–22 | S/C | 1 | 1:04.0 | 1:10.1 |  |
| 6 | 23–24 | S/C | 1 | 1:10.5 | 1:15.4 |  |
| 7 | 25–26 | S/C | 1 | 1:17.0 | 1:23.9 |  |
| 8 | 27–29 | S/C | 1 | 1:23.8 | 1:32.7 |  |
| 9 | 30–32 | T/B | 1 | 1:34.8 | 1:40.3 |  |
| 10 | 32–36 | S/C<br>T/B | 2 | 1:39.2 | 1:46.5 |  |
| 11 | 35–38 | S/C<br>T/B | 2 | 1:45.7 | 1:52.0 |  |
| 12 | 38–40 | S/C<br>T/B | 2 | 1:51.9 | 1:56.2 |  |
| 13 | 40–42 | S/C | 1 | 1:56.2 | 2:00.6 |  |
| 14 | 42–43 | S/C | 1 | 2:00.5 | 2:03.6 |  |
| 15 | 44–47 | S/C | 1 | 2:03.7 | 2:11.2 |  |
| 16 | 47–50 | todos | 1 | 2:11.2 | 2:18.4 |  |
| 17 | 51–55 | S/C<br>T/B<br>T/B | 3 | 2:19.3 | 2:28.1 | três textos simultâneos |
| 18 | 55–63 | S/C<br>T/B<br>T/B | 3 | 2:27.4 | 2:44.7 | três textos simultâneos |
| 19 | 65–67 | S/C | 1 | 2:48.6 | 2:54.7 |  |
| 20 | 67–68 | todos | 1 | 2:55.4 | 3:00.1 |  |
| 21 | 68–71 | todos<br>T/B | 2 | 2:58.5 | 3:10.4 |  |
| 22 | 71–73 | S/C<br>T/B | 2 | 3:07.4 | 3:17.1 |  |
| 23 | 74–75 | S/C | 1 | 3:17.5 | 3:23.3 |  |
| 24 | 76–76 | S/C | 1 | 3:24.2 | 3:27.7 |  |
| 25 | 78–79 | S/C | 1 | 3:30.1 | 3:36.5 |  |
| 26 | 80–81 | S/C | 1 | 3:37.5 | 3:43.6 |  |
| 27 | 82–83 | S/C | 1 | 3:44.4 | 3:49.3 |  |
| 28 | 84–88 | todos | 1 | 3:52.9 | 4:08.0 |  |
| 29 | 89–90 | S/C | 1 | 4:09.5 | 4:15.1 |  |

Elisões nesta música: 25. Sinalizações de acento: 0.

## 6. Amor divino (Final e Reprise) — Love Divine (Finale and Reprise)

Cânticos tradicionais citados (asterisco na partitura): The First Noel (c. 4); Love Divine, All Loves Excelling (c. 31); On Christmas Night All Christians Sing (c. 52).

**Narração 6 (tempo provisório).** Voz M = narrador, F = narradora.

| # | Compasso | Voz | Início | Fim |
|---|---|---|---|---|
| N1 | 5 | M | 0:09.0 | 0:16.2 |
| N2 | 5 | F | 0:16.2 | 0:23.0 |
| N3 | 9 | M | 0:24.0 | 0:25.9 |
| N4 | 9 | M | 0:25.9 | 0:28.1 |
| N5 | 13 | F | 0:28.1 | 0:32.0 |
| N6 | 17 | M | 0:33.0 | 0:37.0 |

**Letra cantada.**

| # | Compassos | Vozes | Linhas | Início | Fim | Observação |
|---|---|---|---|---|---|---|
| 1 | 20–24 | S/C | 1 | 0:39.0 | 0:46.6 |  |
| 2 | 25–29 | S/C | 1 | 0:47.3 | 0:57.9 |  |
| 3 | 30–32 | T/B | 1 | 0:59.7 | 1:03.7 |  |
| 4 | 34–35 | T/B | 1 | 1:05.6 | 1:09.6 |  |
| 5 | 36–38 | S/C | 1 | 1:11.5 | 1:15.5 |  |
| 6 | 39–42 | S/C | 1 | 1:17.4 | 1:23.6 |  |
| 7 | 44–45 | S/C | 1 | 1:25.5 | 1:29.4 |  |
| 8 | 47–47 | S/C | 1 | 1:31.5 | 1:33.8 |  |
| 9 | 49–50 | S/C | 1 | 1:35.3 | 1:39.4 |  |
| 10 | 51–53 | S/C | 1 | 1:40.7 | 1:44.8 |  |
| 11 | 53–55 | S/C | 1 | 1:45.0 | 1:48.7 |  |
| 12 | 55–57 | S/C | 1 | 1:49.0 | 1:52.9 |  |
| 13 | 57–59 | S/C | 1 | 1:53.0 | 1:57.5 |  |
| 14 | 60–60 | S/C | 1 | 1:57.6 | 1:59.9 |  |
| 15 | 61–62 | S/C | 1 | 1:59.9 | 2:03.8 |  |
| 16 | 63–64 | S/C | 1 | 2:03.9 | 2:07.3 |  |
| 17 | 65–66 | S/C | 1 | 2:07.8 | 2:11.7 | acento: "U-na-se" (c. 65), tônica "na" em tempo fraco e "U" na cabeça do compasso |
| 18 | 67–68 | S/C | 1 | 2:11.7 | 2:15.2 |  |
| 19 | 69–70 | S/C | 1 | 2:15.6 | 2:19.5 |  |
| 20 | 70–72 | S/C | 1 | 2:19.5 | 2:23.1 |  |
| 21 | 73–77 | S/C | 1 | 2:23.5 | 2:34.2 |  |
| 22 | 79–79 | T/B | 1 | 2:36.1 | 2:38.1 |  |
| 23 | 80–83 | todos | 1 | 2:38.1 | 2:46.0 |  |
| 24 | 85–86 | S/C | 1 | 2:47.9 | 2:51.2 |  |
| 25 | 86–90 | S/C<br>T/B | 2 | 2:50.7 | 2:59.7 |  |
| 26 | 91–92 | S/C | 1 | 3:01.1 | 3:03.6 |  |

Elisões nesta música: 19. Sinalizações de acento: 1.

## Arquivos de legenda

Na pasta `legendas/`:

| Arquivo | Uso |
|---|---|
| `01_o-amor-desceu_PT.srt` | Legenda da faixa 1, com tempo contado do início do playback da faixa |
| `02_vem-emanuel-vem_PT.srt` | Legenda da faixa 2, com tempo contado do início do playback da faixa |
| `03_da-nos-paz_PT.srt` | Legenda da faixa 3, com tempo contado do início do playback da faixa |
| `04_ouca-a-alegre-cancao_PT.srt` | Legenda da faixa 4, com tempo contado do início do playback da faixa |
| `05_o-amor-seja-seu-e-meu_PT.srt` | Legenda da faixa 5, com tempo contado do início do playback da faixa |
| `06_amor-divino_PT.srt` | Legenda da faixa 6, com tempo contado do início do playback da faixa |
| `00_cantata-completa_PT.srt` | As seis faixas numa linha do tempo só, com os playbacks em sequência como estão (mapa da Etapa 1) |
| `*_conferencia.srt` | Mesmos tempos; cada linha traz as vozes e cada verso fecha com os compassos, para conferir com a partitura original e o áudio |

A legenda completa depende da decisão sobre a pausa entre as faixas (Etapa 1, decisão 2). Se a pausa mudar, as legendas por faixa continuam valendo e a completa é refeita.

## Narração nas legendas

As legendas trazem também o texto da narração em português, em itálico, antes da letra de cada música. O texto é o de `narracao_texto_PT.pdf`, conferido palavra por palavra. A divisão em trechos, as vozes (M/F) e os compassos de entrada seguem `narracao-vozes.md`.

Os tempos da narração são **provisórios**. A gravação em português ainda não existe; por isso cada trecho foi colocado na janela em que o narrador original fala o trecho correspondente (medida na Etapa 1), com o tempo repartido pelo tamanho do texto. Quando a gravação chegar, os tempos da narração são refeitos a partir dela; a letra cantada não muda.

Dois blocos têm mais texto em português do que cabe no tempo do narrador original, a um ritmo normal de leitura (cerca de 13 a 14 caracteres por segundo):

- **Narração 2, 2ª parte** (0:23–0:32): 154 caracteres em 9 s; precisa de cerca de 11 a 12 s. Há folga até a entrada do coro (1:00.5).
- **Narração 6, 2ª parte** (0:24–0:32): 166 caracteres em 8 s; precisa de cerca de 12 s. Aqui não há folga: a última frase ("Paz na terra...") termina perto da entrada do coro (0:38.9). Na gravação, vale começar a 2ª parte logo após a 1ª ou encurtar o texto.

## Pontos para revisão

1. **Músicas 2 e 4:** a conferência automática dos tempos foi menos conclusiva. Vale assistir com a legenda de conferência e anotar qualquer verso adiantado ou atrasado.
2. **Textos simultâneos** (por exemplo, M1 c. 60–64, com três textos ao mesmo tempo): confirmar se o telão mostra todas as linhas ou só a melodia principal.
3. **Acento:** "Una-se" (M4 c. 28 e c. 129; M6 c. 65) e "proclamando" (M4 c. 55). Decidir se fica como está.
4. **Hífens:** a v4 omite o hífen em alguns fins de sistema e em sílabas muito juntas (por exemplo "No_ el," na M6 c. 20). Na legenda essas sílabas foram juntadas pela palavra que formam; vale conferir na legenda de conferência.

Total: 184 versos de legenda nas seis músicas.
