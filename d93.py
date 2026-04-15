jogador = {}
jogador['nome'] = input('Nome: ')
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
g = []

for i in range(0, partidas):
    g.append(int(input(f'Quantos gols {jogador['nome']} fez na partida {i + 1}? ')))


jogador['gols'] = g[:]
jogador['total'] = sum(g)

print('=-'*40)
print(jogador)
print('=-'*40)

for i, n in jogador.items():
    print(f'o campo {i} tem o valor {n}')

print('=-'*40)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas:')

for i in range(0, partidas):
    print(f'Na partida {i + 1}, fez {g[i]} gols')

print(f'Foi um total de {jogador['total']} gols')
