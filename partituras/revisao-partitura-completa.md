# Revisão da partitura completa (coro e piano) — v3

Arquivo: `partituras\partitura-completa_o-amor-desceu_PT_v3.pdf` (74 páginas, as seis músicas). Montado a partir dos PDFs do maestro.

O nome é v3 porque já existe na pasta um `..._PT_v2.pdf` que não saiu desta montagem: é a v1 com outro nome, sem a música 5. Esse arquivo não foi tocado. A v1 (64 p., sem a música 5) também continua na pasta.

**Referência de letra:** a partitura só de vozes (v4), que é a versão mais atualizada da letra.

| Parte | Páginas |
|---|---|
| Capa, prefácio e índice | 1–3 |
| Música 1 | 4–14 |
| Música 2 | 15–28 |
| Música 3 | 29–37 |
| Música 4 | 38–50 |
| Música 5 | 51–60 |
| Música 6 | 61–70 |
| Narração completa | 71–72 |
| Créditos | 73 |
| Contracapa | 74 |

**Arquivos de apoio:**
- Recortes lado a lado (antes | depois | original), um por música: `partituras\edicao-completa\recortes\`.
- Script de montagem: `partituras\edicao-completa\scripts-montagem-edicao-completa.zip`. Use junto com o `kit-ferramentas.zip`. O comando é `python3 -I full/build.py`.

---

## 1. Correções aplicadas (repetir no Sibelius)

Sem estas correções no arquivo do Sibelius, a próxima exportação traz os erros de volta.

| # | Música, compasso, pauta | Como estava no arquivo | Como ficou |
|---|---|---|---|
| A1 | M1, c. 103, Soprano/Contralto | 2ª e 3ª notas Sol4 | Lá4, igual ao c. 23 |
| D1 | M1, c. 24, Tenor | linha diferente do original | Lá, Lá, Dó–Si em colcheias (Sol no tempo seguinte); letra "o a-mor des-", como na v4 |
| A2 | M2, c. 105, Baixo | Si sem bequadro (2º tempo) | ♮ no Si |
| A3 | M2, c. 119, Baixo | Si sem bequadro (colcheia do 2º tempo) | ♮ no Si |
| A4 | M2, c. 138, Soprano/Contralto | ♮ no Dó | sem bequadro: o Dó♯ vem ligado do c. 137 |
| A5 | M6, c. 81, Tenor | Fá♭ e ♮ de precaução no c. 82 | Fá natural, sem os dois acidentes |
| P1 | M4, c. 4, piano mão esquerda (acorde de semibreves) | faltava o Mi♭4 | Mi♭4 acrescentado; o Fá4 foi para a coluna da direita, com as linhas suplementares estendidas |
| P2 | M5, c. 15, piano mão esquerda | faltavam as duas ligaduras de valor Si♭~Si♭ (4ª para 5ª semicolcheia de cada metade) | ligaduras acrescentadas, com o mesmo desenho das do c. 14 |
| P3 | M5, c. 91, piano mão direita (acorde final) | faltavam o Si♭4 e o Mi♭5 | os dois acrescentados; o Si♭4 fica na coluna da direita, como o arquivo já faz com o Si♭5; o acorde fica com as 8 notas do original |
| L1 | M4, c. 74–75, Tenor/Baixo | "Deusquer" como uma sílaba só | "Deus" / "quer" / "nos", cada sílaba sob a sua nota |
| L2 | M4, c. 152, Soprano/Contralto | "tal!!!" | "tal!" |
| L3 | M5, c. 23, letra entre as pautas vocais | redigitada à mão: "E esse amor é seu e meu" | igual à v4: **"E‿e-le é___ seu e meu."** |

### L3 em detalhe

No arquivo do maestro, a linha do c. 23 foi redigitada à mão em outra fonte (Minion). Tinha hífens soltos e um sublinhado no lugar de elisão. Uma anotação de caneta branca apagava, por cima, as ligaduras do 3º–4º tempo em S/C e em T/B.

O que foi feito:
- A letra ficou igual à v4.
- O texto está na fonte do arquivo, com a curva de elisão e o traço de extensão do "é".
- As ligaduras do 3º–4º tempo continuam em S/C e em T/B, como na v4 e no original.
- A anotação de caneta e o texto redigitado saíram do arquivo.

No Sibelius, o c. 23 tem de voltar ao texto da v4.

### Textos e cabeçalhos corrigidos

- M4: "OUÇAM A ALEGRE CANÇÃO" → "OUÇA A ALEGRE CANÇÃO".
- M6: "(Finale e Reprise)" → "(Final e Reprise)".
- Músicas 3 e 4: o rodapé "Copyright © 2026 por [Titular…]" saiu. Todas as primeiras páginas têm "© 2014 Lorenz Publishing Company. Todos os direitos reservados."
- A numeração do Sibelius no alto das páginas foi removida. A numeração contínua fica no rodapé.

### Andamentos e agógica

Todos foram conferidos lado a lado com o original. Ficam acima das vozes e acima do piano, no estilo do arquivo: palavra em redondo + ♩ = n. Em compasso que começa com troca de armadura ou fórmula, a marca entra depois dela.

**M1**
- c. 1: Livremente ♩ = 88-92.
- c. 7: Um pouco mais rápido ♩ = 100.
- c. 17: Com intensidade contida ♩ = 116.
- c. 69: Um pouco mais amplo ♩ = 112.
- c. 89: Um pouco mais lento ♩ = 108.
- c. 95: Grandioso ♩ = 100.
- c. 99: Com movimento ♩ = 108.
- c. 109: Lentamente ♩ = 96.
- c. 110: rit.
- c. 111: *livremente*, com *mp* nas vozes.

**M2**
- c. 1: Livremente ♩ = 88.
- c. 7: Suavemente ♩ = 96.
- c. 22: Misterioso ♩ = 144.

**M3**
- c. 1: Calmamente ♩ = 96.
- c. 17: Ternamente ♩ = 100.
- c. 25: *Coro infantil (opcional) – uníssono ou solo*.
- c. 41: *fim do coro infantil*.
- c. 86: *a tempo – SA + coro infantil (opcional)*.
- c. 108: Decidido ♩ = 96.

**M4**
- c. 1: Calmamente ♩ = 92.
- c. 5: Com energia ♩ = 108.
- c. 4, 9 e 14: rit.
- c. 10: *a tempo*.
- c. 16: Leve e animado 𝅗𝅥 = 76.
- c. 124: poco rit.
- c. 125: a tempo.
- c. 139: rit.
- c. 143: Um pouco mais lento 𝅗𝅥 = 72.

**M5** (a anacruse inicial é o c. 0)
- c. 0: Ternamente ♩ = 66.
- c. 8: rit.
- c. 9: Tranquilo ♩ = 72.
- c. 20: poco rit.
- c. 21: *a tempo*.
- c. 28: rit.
- c. 29: Suavemente ♩. = 52.
- c. 50: rit.
- c. 51: *a tempo*, acima do *mp*.
- c. 65: poco rit.
- c. 67: Tranquilo ♩ = 72.
- c. 83: molto rit.
- c. 84: *a tempo*.
- c. 87: Tranquilo ♩ = 72.
- c. 89: rit.
- O "A tempo" em negrito do arquivo virou *a tempo* em itálico.

**M6**
- c. 1: Calmamente ♩ = 92.
- c. 29: Animado ♩ = 120.
- c. 61: Com energia ♩ = 120-124.
- c. 79: *a tempo*, nas vozes e no piano.

## 2. Diferenças em relação ao original mantidas como adaptação

- D2 (M2, c. 124 e c. 180) e D3 (M5, c. 26), como na v4.
- Notas divididas para caber as sílabas em português, e a curva de elisão no lugar do hífen.
- M4: alternância "Na-tal" / "na-tal".
- Capa "O Amor Desceu no Natal" × miolo "O Amor desceu".
- Narrações 2 e 3: foi usado o texto do grupo, sem completar.
- Títulos dos cânticos em inglês, com nota de rodapé em português, numerada por página. Na M5: *The First Noel* (c. 0), *Love Came Down at Christmas* (c. 13) e *Gesù Bambino* (c. 33).
- Narração na partitura:
  - Começa no ponto de entrada do Anexo A, na cor de cada voz.
  - Fica entre as pautas vocais vazias, ou acima do sistema, ou acima do piano.
  - Triângulo de entrada em M3 c. 6, M4 c. 3 e M6 c. 5.
  - Na M5, o fim da última frase passa para o sistema do c. 11, para não ficar uma palavra sozinha.
- Reduções de página:
  - M1: p. 4 (1,2%), p. 9 (1,6%), p. 11 (1,1%) e p. 14 (1,4%).
  - M2: p. 28 (2,9%).
  - M3: p. 37 (0,8%).
  - A M5 não precisou de redução.

## 3. Pontos para o maestro decidir

1. **M4, c. 5 e M6, c. 61**: o original diz *With urgency* ("Com urgência"). Ficou "Com energia", a expressão do próprio arquivo. Confirmar.
2. **Agógica em lugar diferente do original**, mantida como está no arquivo:
   - M2: accel. no c. 11 e no c. 13 (no original, no c. 17).
   - M2: rit. no c. 6 e no c. 20 (no original, no c. 9 e no c. 24).
3. **Dinâmicas, articulações e pedal do original que faltam no arquivo** (corrigir no Sibelius):
   - M4: *mp* no c. 1, *p* no c. 5, *mp* no c. 10 e *mf* no c. 16.
   - M6: *p* no piano no c. 1, e respiração nas vozes antes do c. 61.
   - Staccatos: M2, c. 120–125; M4, c. 23–34 e c. 74–75.
   - M5, dinâmicas:
     - c. 0: *p*.
     - c. 9: *mp*.
     - c. 25: *f*.
     - c. 49: *f*.
     - c. 51: *mp*.
     - c. 65: *mp*.
     - c. 67: *p*.
     - c. 78: *ff*.
     - c. 84: *mf*.
     - c. 87: *mp*.
     - c. 91: *p*.
   - M5, outros:
     - Reguladores nos c. 24 e 29.
     - Pedal nos c. 90–91.
4. **M2, c. 202–203, mão esquerda**: ligadura de valor não confirmada. Conferir no Sibelius.

## 4. O que foi conferido e como

**Vozes.** Comparação vetor com vetor, por compasso e por pauta, contra a v4 vocal.
- M1–M4 e M6: 1071 compassos-pauta iguais e 10 diferenças, todas do programa de leitura.
- M5: 145 iguais e 4 diferenças, todas do programa de leitura (c. 41, 43, 46 e 55).

**Letra.** A referência é a v4 vocal.
- Contagem de todas as sílabas de cada música, edição × v4: as seis músicas batem.
- As diferenças que restam são só de extração do texto do PDF, por exemplo "pazDeusquer" e "enche", que a v4 junta numa palavra só.
- As sílabas de cada compasso também foram comparadas com a v4.

**Piano.** 1584 compassos-pauta.
- M1–M4 e M6:
  - 1225 iguais pela máquina.
  - Os 175 sinalizados e uma amostra de 128 foram vistos a olho.
  - Erro real encontrado: P1.
- M5:
  - 144 iguais pela máquina.
  - Os 40 sinalizados foram vistos a olho.
  - Erros reais encontrados: P2 e P3.

**Compassos por música:** 115, 203, 135, 153, 92 (c. 0–91) e 94, iguais ao original.

**Montagem.**
- Todas as páginas foram renderizadas e vistas.
- 33 links, com `/NM` único.
- O índice não tem mais "(partitura a incluir)".
- Marcadores, metadados e numeração das páginas conferidos.
- A busca de restos no texto (Titular, Ligeiram, OUÇAM, !!!, "A tempo" em negrito) não achou nada.
- Nenhum texto acrescentado cobre nota, ligadura ou dinâmica.
- `qpdf --check` sem erros.
