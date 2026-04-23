#jeito que eu fiz
"""def jogador(nome = None, gols = None):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = input('Nome do jogador: ')
g = input('Número de gols: ')

jogador(n, g)"""

#jeito do professor
def jogador(nome='<desconhecido>', gol=0):
    """
    Descreve o nome e os gols de um jogador.
    nome: Nome do jogador
    gol: Gols realizados pelo jogador.
    """
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


n = input('Nome do jogador: ')
g = input('Número de gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    jogador(gol=g)
else:
    jogador(n, g)

help(jogador)