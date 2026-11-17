# Cantata "O Amor Desceu" – Vídeo de acompanhamento

Repositório com todos os arquivos necessários para produzir o **vídeo de acompanhamento da Cantata de Natal 2026** do grupo **Herdeiros**.

Aqui ficam os materiais de produção: playbacks, narrações, vídeos, projeto do editor de vídeo, legendas/versos e demais arquivos de apoio.

## Ferramentas

- **Edição de vídeo:** [Clipchamp](https://clipchamp.com/pt-br/) – limitado, porém intuitivo e gratuito. Foi escolhido em vez do Adobe, considerado profissional e caro demais para este projeto.
- **Edição de áudio (narrações):** [Audacity](https://www.audacityteam.org/)
- **Música/playbacks (possível):** Suno, caso as versões atuais não fiquem como esperado, assim que as legendas e os versos estiverem prontos.
- **Repositório:** GitHub, para todos acessarem os arquivos, não só quem programa.

## Fontes de vídeos

- [Mídia da Igreja de Jesus Cristo dos Santos dos Últimos Dias](https://www.churchofjesuschrist.org/media/video?lang=eng)
- [Pixabay – vídeos](https://pixabay.com/pt/videos/search/)
- [Pexels – vídeos](https://www.pexels.com/pt-br/videos/)


## Estrutura do repositório

```
cantata-o-amor-desceu/
├── README.md
├── partituras/
│   ├── revisao-partitura-PT.md        # revisão da partitura em português (v2 → v3) contra a original
│   ├── auditoria-v3.md                # auditoria da versão definitiva contra a original
│   └── revisao-partitura-completa.md  # revisão da partitura completa (coro e piano)
├── kits-de-voz/
│   └── kits-de-voz.md         # como os kits de voz foram feitos e o que há em cada um
├── roteiro/
│   ├── etapa-1-estrutura.md   # ordem das músicas, durações, narração e mapa geral de tempos
│   ├── mapa-de-tempos.json    # os mesmos tempos, em segundos, para scripts
│   ├── etapa-2-letras.md      # letras alinhadas: compassos, vozes e tempo de cada verso (sem o texto)
│   ├── playback-continuo.md   # faixa única com os seis playbacks e as pausas do original
│   └── playback-continuo.json # início de cada playback na faixa única, em segundos
├── scripts/                   # scripts das Etapas 1 e 2 (ver scripts/README.md)
└── ...                        # playbacks, narrações, vídeos, projeto do editor (fora do repositório)
```

O repositório é público. Por isso ficam fora dele os arquivos de áudio e vídeo, as partituras e tudo o que traz a letra ou o texto da narração (legendas .srt, versão da Etapa 2 com a letra). Esse material está no Drive do projeto.

## Padrão de nomes

Arquivos por faixa seguem `NN_titulo-da-musica_tipo.ext`, em que NN é o número da faixa na ordem da cantata, sem acentos e sem espaços. Exemplo: `03_da-nos-paz_playback.mp3`.

| NN | Música | Trecho do nome |
|---|---|---|
| 01 | O Amor desceu (Abertura) | `o-amor-desceu` |
| 02 | Vem, Emanuel, vem | `vem-emanuel-vem` |
| 03 | Dá-nos paz | `da-nos-paz` |
| 04 | Ouça a alegre canção | `ouca-a-alegre-cancao` |
| 05 | O Amor seja seu e meu | `o-amor-seja-seu-e-meu` |
| 06 | Amor divino (Finale e Reprise) | `amor-divino` |
