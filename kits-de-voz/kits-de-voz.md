# Kits de voz — O Amor desceu

Situação em 16/11/2026: kits das 6 músicas prontos na pasta `kits-de-voz` da cantata, com os pacotes .zip já gerados em `kits-de-voz\pacotes`. Os arquivos de áudio ficam fora deste repositório.

## O que é cada faixa
- Linha do naipe (piano + coro "aah", altura real, sem letra) por cima da gravação cantada (+10 dB) e por cima do playback (+7 dB).
- Notas lidas da partitura vocal em português (v4), com ligaduras de valor, quiálteras e acidente passando pela ligadura. Tempo alinhado à gravação cantada (erro médio 29–40 ms).

## Divisão das vozes (regra do grupo)
Por número de notas na pauta: 1 nota → todos; 2 → 1ª e 2ª voz na de cima, 3ª e 4ª na de baixo; 3 → 1ª e 2ª na de cima, 3ª no meio, 4ª embaixo; 4 → uma cada.
Mulheres: 1º soprano, 2º soprano, 1º contralto, 2º contralto. Homens: 1º tenor, 2º tenor, barítono, baixo.
Quando 1ª e 2ª voz nunca se separam numa música, sai uma faixa só (`soprano`, `tenor`).

## Faixas por música
| Música | Faixas |
|---|---|
| 1 | soprano, contralto 1, contralto 2, tenor, barítono, baixo |
| 2 | soprano, contralto 1, contralto 2, tenor, barítono, baixo |
| 3 | soprano, contralto 1, contralto 2, tenor, barítono, baixo, coro infantil/solo (c. 25–41) |
| 4 | soprano, contralto 1, contralto 2, tenor, barítono, baixo, descante (c. 125–136) |
| 5 | soprano, contralto 1, contralto 2, tenor, barítono, baixo |
| 6 | soprano 1, soprano 2, contralto 1, contralto 2, tenor, barítono, baixo, descante opcional (c. 69–72) |

## Pacotes
`NN_<musica>_gerar-pacotes.bat` (um por música) e `00_gerar-todos-os-pacotes.bat` criam em `kits-de-voz\pacotes\NN_<musica>\` um .zip por naipe (cantado + playback) e um `_completo.zip`.

## Correção de letra: M6, c. 76–77, tenores
Deve ser "Sim, nas-ceu Je-sus!" (Sim = Ré, nas = Mi, ceu = Ré, Je = Dó, sus = Si♮). Antes estava só "Nas-ceu Je-sus!", com a primeira semínima sem sílaba.
- Corrigido em 16/11 em `partituras\partitura-grupo_o-amor-desceu_PT_v5_definitiva.pdf` (p. 37) e `partituras\partitura-completa_o-amor-desceu_PT_v4.pdf` (p. 68). Só essa linha mudou; o resto das páginas é igual às versões anteriores.
- Falta repetir no arquivo do Sibelius.

## Voz cantada com letra
- Teste 1 (16/11): voz sintética (espeak-ng/MBROLA + WORLD), soprano da música 6, c. 19–49. Afinação certa, timbre robótico. Reprovado.
- Teste 2 (16/11): OpenUtau 0.1.576 (portátil, em `voz-cantada\OpenUtau`) com a voz DiffSinger Apollo DS 1.0 (barítono, português brasileiro) e o fonemizador DiffSinger em português. Tenor da música 6 inteiro, com "Sim, nas-ceu Je-sus!".
  - Projeto `voz-cantada\06_amor-divino_tenor.ustx`, gerado com notas, letra sílaba por sílaba (melisma = "+") e mapa de tempo do kit.
  - Exportado com Arquivo › Exportar Áudio › Exportar Arquivos Wav; o arquivo sai em `voz-cantada\Export`.
  - Afinação medida: erro mediano 1,3 cents.
  - Resultado em `voz-cantada\06_amor-divino_tenor_voz-apollo_*.mp3`, aguardando escuta.
- Licença: os termos da Apollo proíbem conteúdo religioso, com exceção de cânticos ecumênicos. A cantata foi declarada ecumênica pelo grupo, e o uso seguiu com base nisso.
- Outras vozes em português (Lenz Blair, Umidaji (feminina), KYANN) proíbem uso religioso sem exceção. Ainda falta uma voz feminina em português com licença compatível para sopranos e contraltos.
