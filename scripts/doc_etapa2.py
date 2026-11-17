"""Gera roteiro/etapa-2-letras.md a partir de etapa2.json.
Uso: python3 -I doc_etapa2.py <etapa2.json> <saida.md>"""
import json, os, sys

SEM_LETRA = bool(os.environ.get("SEM_LETRA"))   # versão pública: sem o texto da letra e da narração

TIT = {1: ("O Amor desceu (Abertura)", "Love Came Down (Opener)"), 2: ("Vem, Emanuel, vem", "Come, Emmanuel, Come (Hope)"),
       3: ("Dá-nos paz", "Grant Us Peace (Peace)"), 4: ("Ouça a alegre canção", "Listen to the Joyful Song (Joy)"),
       5: ("O Amor seja seu e meu", "Love Be Yours, Love Be Mine (Love)"), 6: ("Amor divino (Final e Reprise)", "Love Divine (Finale and Reprise)")}
SLUG = {1: "01_o-amor-desceu", 2: "02_vem-emanuel-vem", 3: "03_da-nos-paz", 4: "04_ouca-a-alegre-cancao",
        5: "05_o-amor-seja-seu-e-meu", 6: "06_amor-divino"}
VOZ = {"M": "S/C", "H": "T/B", "Desc": "Desc.", "M+H": "todos", "Desc+M": "Desc. + S/C", "Desc+M+H": "todos + Desc."}


def mmss(t):
    m, s = divmod(t, 60)
    return f"{int(m)}:{s:04.1f}"


d = json.load(open(sys.argv[1]))
L = []
A = L.append
A("# Cantata \"O Amor desceu\" — Etapa 2: Letras alinhadas")
A("")
A("Situação: entregue para aprovação em 14/11/2026, adiantada antes da aprovação formal da Etapa 1. Base: partitura do grupo `partitura-grupo_o-amor-desceu_PT_v4_definitiva.pdf` e gravação cantada de referência.")
if SEM_LETRA:
    A("")
    A("**Versão pública, sem a letra.** Este repositório é público e a letra em português é tradução de obra com direitos da Lorenz; por isso aqui ficam só compassos, vozes e tempos. A versão com a letra, as legendas .srt e os vídeos de conferência estão no Drive do projeto (pasta `roteiro` e `legendas`). Os scripts em `scripts/` regeram tudo a partir da partitura e dos áudios.")
A("")
A("## Como ler")
A("")
A("- Cada linha da tabela é um verso como aparece na legenda. Quando vozes cantam textos diferentes ao mesmo tempo, a legenda mostra duas ou três linhas.")
A("- **Vozes:** S/C = sopranos e contraltos (pauta de cima), T/B = tenores e baixos, Desc. = descante, todos = mesmo texto nas duas pautas.")
A("- **Início e fim:** tempo dentro do arquivo de playback da faixa (m:ss.s), do primeiro ataque à última nota do verso. Na legenda, cada verso aparece 0,25 s antes e fica até 0,4 s depois.")
A("- **Compassos:** numeração da partitura do grupo, igual à da partitura original Lorenz (as seis músicas têm o mesmo número de compassos, conforme a revisão).")
A("")
A("## Letra original em inglês")
A("")
A("A tabela não traz a coluna com a letra em inglês. A letra original é de 2014, com direitos da Lorenz, e não a transcrevo. Para conferir verso a verso, use a coluna **Compassos** com a partitura original licenciada, ou a legenda de conferência, que traz compassos e vozes ao lado do português. Os cânticos tradicionais citados em cada música estão listados pelo título.")
A("")
A("## Como os tempos foram gerados")
A("")
A("1. Letra, notas e compassos foram lidos direto do PDF vetorial da v4. O texto apagado por camada branca nas correções foi descartado.")
A("2. A voz foi isolada da gravação cantada subtraindo o playback alinhado.")
A("3. A partitura foi alinhada à voz isolada por comparação de alturas (croma) ao longo do tempo, a partir da entrada do coro de cada música. O mapa compasso a compasso foi suavizado para eliminar barras deslocadas.")
A("4. Conferência: nas músicas 1, 3, 5 e 6, o início dos versos bate com a subida de energia da voz, com mediana entre −0,07 e 0 s. Nas músicas 2 e 4 a voz isolada tem mais resto de acompanhamento e a conferência automática é menos conclusiva; onde há subida nítida, o erro fica até 0,2 s.")
A("5. A gravação de referência é em inglês. Como o português segue as mesmas notas, o tempo de cada sílaba vem da posição da nota na partitura. Onde o grupo dividiu uma nota para caber sílabas, o tempo da sílaba extra é estimado pela posição na pauta.")
A("")
A("## Métrica e prosódia")
A("")
A("A v4 já traz cada sílaba em português sob uma nota, então não há sílaba sobrando. O que foi verificado:")
A("")
A("- **Acento:** palavras com a sílaba tônica em tempo fraco enquanto uma sílaba átona (que não seja acento secundário) cai na cabeça do compasso. Aparecem na coluna Observação.")
A("- **Ritmo alterado para caber o português:** segundo a auditoria da v3, 46 compassos-pauta dividem uma nota do original em duas para caber as sílabas, além das adaptações D2 (M2 c. 124 e c. 180) e D3 (M5 c. 26). A auditoria não lista os 46 compassos; para sinalizá-los verso a verso é preciso essa lista.")
A("- **Elisões** (duas vogais numa nota, marcadas com _ na partitura): contadas por música. São normais no canto em português e não foram tratadas como problema.")
A("")
tot_v = 0
for m in map(str, range(1, 7)):
    r = d[m]
    pt, en = TIT[int(m)]
    gs = r["grupos"]
    tot_v += len(gs)
    A(f"## {m}. {pt} — {en}")
    A("")
    if r["citacoes"]:
        A("Cânticos tradicionais citados (asterisco na partitura): " + "; ".join(c['titulo'] if "(c." in c['titulo'] else f"{c['titulo']} (c. {c['compasso']})" for c in r["citacoes"]) + ".")
        A("")
    if r.get("narracao"):
        A(f"**Narração {m} (tempo provisório).** Voz M = narrador, F = narradora.")
        A("")
        A("| # | Compasso | Voz | " + ("" if SEM_LETRA else "Texto | ") + "Início | Fim |")
        A("|---|---|---|" + ("" if SEM_LETRA else "---|") + "---|---|")
        for i, it in enumerate(r["narracao"], 1):
            tx = "" if SEM_LETRA else f"{it['texto']} | "
            A(f"| N{i} | {it['compasso']} | {it['voz']} | {tx}{mmss(it['ini'])} | {mmss(it['fim'])} |")
        A("")
        A("**Letra cantada.**")
        A("")
    A("| # | Compassos | Vozes | " + ("Linhas" if SEM_LETRA else "Português (grupo)") + " | Início | Fim | Observação |")
    A("|---|---|---|---|---|---|---|")
    for i, g in enumerate(gs, 1):
        txt = str(len(g["linhas"]) + len(g.get("extra", []))) if SEM_LETRA else "<br>".join(g["linhas"] + g.get("extra", []))
        vz = "<br>".join(VOZ.get(v, v) for v in g["vozes"])
        obs = []
        for s in r["sinal"]:
            if g["c_ini"] <= s["compasso"] <= g["c_fim"]:
                obs.append(f"acento: \"{s['palavra']}\" (c. {s['compasso']}), tônica \"{s['tonica']}\" em tempo fraco e \"{s['forte']}\" na cabeça do compasso")
        if len(g["linhas"]) + len(g.get("extra", [])) >= 3:
            obs.append("três textos simultâneos")
        A(f"| {i} | {g['c_ini']}–{g['c_fim']} | {vz} | {txt} | {mmss(g['ini'])} | {mmss(g['fim'])} | {'; '.join(obs)} |")
    A("")
    A(f"Elisões nesta música: {len(r['elisoes'])}. Sinalizações de acento: {len(r['sinal'])}.")
    A("")
A("## Arquivos de legenda")
A("")
A("Na pasta `legendas/`:")
A("")
A("| Arquivo | Uso |")
A("|---|---|")
for m in range(1, 7):
    A(f"| `{SLUG[m]}_PT.srt` | Legenda da faixa {m}, com tempo contado do início do playback da faixa |")
A("| `00_cantata-completa_PT.srt` | As seis faixas numa linha do tempo só, com os playbacks em sequência como estão (mapa da Etapa 1) |")
A("| `*_conferencia.srt` | Mesmos tempos; cada linha traz as vozes e cada verso fecha com os compassos, para conferir com a partitura original e o áudio |")
A("")
A("A legenda completa depende da decisão sobre a pausa entre as faixas (Etapa 1, decisão 2). Se a pausa mudar, as legendas por faixa continuam valendo e a completa é refeita.")
A("")
A("## Narração nas legendas")
A("")
A("As legendas trazem também o texto da narração em português, em itálico, antes da letra de cada música. O texto é o de `narracao_texto_PT.pdf`, conferido palavra por palavra. A divisão em trechos, as vozes (M/F) e os compassos de entrada seguem `narracao-vozes.md`.")
A("")
A("Os tempos da narração são **provisórios**. A gravação em português ainda não existe; por isso cada trecho foi colocado na janela em que o narrador original fala o trecho correspondente (medida na Etapa 1), com o tempo repartido pelo tamanho do texto. Quando a gravação chegar, os tempos da narração são refeitos a partir dela; a letra cantada não muda.")
A("")
A("Dois blocos têm mais texto em português do que cabe no tempo do narrador original, a um ritmo normal de leitura (cerca de 13 a 14 caracteres por segundo):")
A("")
A("- **Narração 2, 2ª parte** (0:23–0:32): 154 caracteres em 9 s; precisa de cerca de 11 a 12 s. Há folga até a entrada do coro (1:00.5).")
A("- **Narração 6, 2ª parte** (0:24–0:32): 166 caracteres em 8 s; precisa de cerca de 12 s. Aqui não há folga: a última frase (\"Paz na terra...\") termina perto da entrada do coro (0:38.9). Na gravação, vale começar a 2ª parte logo após a 1ª ou encurtar o texto.")
A("")
A("## Pontos para revisão")
A("")
A("1. **Músicas 2 e 4:** a conferência automática dos tempos foi menos conclusiva. Vale assistir com a legenda de conferência e anotar qualquer verso adiantado ou atrasado.")
A("2. **Textos simultâneos** (por exemplo, M1 c. 60–64, com três textos ao mesmo tempo): confirmar se o telão mostra todas as linhas ou só a melodia principal.")
A("3. **Acento:** \"Una-se\" (M4 c. 28 e c. 129; M6 c. 65) e \"proclamando\" (M4 c. 55). Decidir se fica como está.")
A("4. **Hífens:** a v4 omite o hífen em alguns fins de sistema e em sílabas muito juntas (por exemplo \"No_ el,\" na M6 c. 20). Na legenda essas sílabas foram juntadas pela palavra que formam; vale conferir na legenda de conferência.")
A("")
A(f"Total: {tot_v} versos de legenda nas seis músicas.")
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(L) + "\n")
print("ok", tot_v)
