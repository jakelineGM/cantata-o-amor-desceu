# Cantata "O Amor Desceu" – Vídeo de acompanhamento

Repositório com todos os arquivos necessários para produzir o **vídeo de acompanhamento da Cantata de Natal 2026** do grupo **Herdeiros**.

Aqui ficam os materiais de produção: playbacks, narrações, vídeos, projeto do editor de vídeo, legendas/versos e demais arquivos de apoio.

## Ferramentas

| Para quê | Ferramenta | Onde baixar |
|---|---|---|
| Edição de vídeo | **Shotcut** (gratuito, código aberto) | <https://www.shotcut.org/download/> |
| Baixar e atualizar o projeto | Git | |


> O projeto foi feito na versão **26.11** do Shotcut. Use essa versão ou uma mais nova; versões muito antigas podem não abrir o arquivo.
> No site do Shotcut, escolha o instalador para o seu sistema (Windows, macOS ou Linux).

## Fontes de vídeos

- [Mídia da Igreja de Jesus Cristo dos Santos dos Últimos Dias](https://www.churchofjesuschrist.org/media/video?lang=eng)
- [Pixabay – vídeos](https://pixabay.com/pt/videos/search/)
- [Pexels – vídeos](https://www.pexels.com/pt-br/videos/)

## Como trabalhar com o projeto

### 1. Baixar o projeto pela primeira vez

1. Instale o **Git** e o **Shotcut** (links acima).
2. Escolha uma pasta com bastante espaço livre (os vídeos passam de **1,5 GB**) e rode:

   ```
   git clone https://github.com/jakelineGM/cantata-o-amor-desceu.git
   ```

   Ou, no GitHub Desktop: *File → Clone repository → URL* e cole o endereço acima.
3. Aguarde terminar. Não interrompa o download; ele traz playbacks, vídeos e o projeto.

### 2. Abrir a última versão do projeto

A última versão foi criada em 23/11 possui as três primeiras músicas e a primeira narração:

```
shotcut/cantata-o-amor-desceu/cantata-o-amor-desceu-3m-1n.mlt
```

Não abra os arquivos de `versoes-anteriores-local/`: são cópias de segurança antigas.

Antes de abrir, atualize o repositório (isso traz o trabalho dos outros):

```
git pull
```

No Shotcut: *Arquivo → Abrir arquivo* e escolha o `.mlt` acima.

### 3. Se o Shotcut disser que há arquivos ausentes

O projeto guarda o **caminho completo** de cada vídeo e áudio (por exemplo `C:/Users/jgdm0/Videos/cantata-o-amor-desceu/...`). Quem clonar em outro lugar ou com outro nome de usuário verá "arquivos ausentes". Faça o seguinte:

Selecione as seguintes pastas:
`playbacks`
`videos\1-o-amor-desceu`
`videos\2-vem-emanuel-vem`
`videos\3-da-nos-paz`

Baixe os seguintes vídeos na qualidade máxima e salve dentro de `videos\1-o-amor-desceu`:
- https://www.churchofjesuschrist.org/media/video/2011-10-0067-the-nativity?lang=eng&collection=bible-videos-nativity
- https://www.churchofjesuschrist.org/media/video/2019-09-0050-the-christ-child-a-nativity-story-lighttheworld?lang=eng&collection=christmas-messages

Depois disso não deve haver problemas de arquivos ausentes.


### 4. Regras de ouro para não perder trabalho

1. Rode `git pull` **antes** de começar a editar.
2. Salve sempre em `shotcut/cantata-o-amor-desceu/`. O Shotcut grava os caminhos desta máquina; avise o grupo antes de enviar um projeto novo.
3. **Só uma pessoa edita o `.mlt` por vez.** O arquivo não é feito para juntar edições de duas pessoas; combinem no grupo quem está com a vez.
4. Ao terminar, envie:

   ```
   git add .
   git commit -m "descreva o que mudou"
   git push
   ```
5. Guarde cópias de segurança antigas só em `versoes-anteriores-local/`, para não misturar com a versão atual.
6. Vídeos novos entram em `videos/<número>-<nome-da-música>/`. Vídeos que testamos e não usamos vão em `videos/nao-usados/` (não sobem ao GitHub).

## Estrutura do repositório

```
cantata-o-amor-desceu/
├── README.md
├── biblioteca-cenas/    # instruções, catálogo e prévias das 519 cenas de apoio (vídeos no Drive)
├── playbacks/           # playbacks em MP3 de cada música
├── roteiro/             # roteiro visual (Etapa 3): cena, fonte e intenção de cada momento
├── shotcut/             # projeto do editor (.mlt) e versões anteriores
├── videos/              # vídeos usados no projeto, organizados por música
│   ├── 1-o-amor-desceu/
│   ├── 2-vem-emanuel-vem/
│   ├── 3-da-nos-paz/
│   └── nao-usados/      # fora do GitHub
└── narracao/            # texto da narração (fora do GitHub)
```

**Cenas de apoio:** comece por [`biblioteca-cenas/README.md`](biblioteca-cenas/README.md). Lá estão as pastas por tema, as prévias numeradas, a minutagem útil dos filmes bíblicos, as regras para não repetir cenas e o padrão da letra grande no centro da tela.

## Andamento do vídeo

| item | video | playback | legenda | audio narracao |ajuste pos revisão|
|---|---|---|---|---|---|
| n1 | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 🟡 |
| m1 | ✅ | ✅ | ⬜ | ⬜ | ⬜ | ⬜ |
| n2 | ⬜ | ✅ | ⬜ | ⬜ | ⬜ | ⬜ |
| m2 | ✅ | ✅ | ⬜ | ⬜ | ⬜ | ⬜ |
| n3 | ⬜ | ✅ | ⬜ | ⬜ | ⬜ | ⬜ |
| m3 | ✅ | ✅ | ⬜ | ⬜ | ⬜ | ⬜ |
| n4 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| m4 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| n5 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| m5 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| n6 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| m6 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
Legenda: ✅ feito · 🟡 em andamento · ⬜ a fazer. Atualize esta tabela a cada etapa concluída.
