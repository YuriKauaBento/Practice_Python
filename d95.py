
j = {}
jogadores = []
partidas = []

while True:
    j.clear()
    j['Nome'] = input('Nome do jogador: ')
    tot = int(input(f'Quantas partidas {j["Nome"]} jogou? '))
    for i in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {i}: ')))
    j['Gols'] = partidas[:]
    j['Total'] = sum(j['Gols'])
    jogadores.append(j.copy())
    partidas.clear()
    op = input('Quer continuar?[S/N]: ')
    while op.strip().upper() not in 'SN':
        op = input('Erro! Digite Apenas S ou N: ')
    if op.strip().upper() == 'N':
        break

print('=-'*40)
print('Cod.', end='')
for i in j.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(jogadores):
    print(f'{k:>4} ', end='')
    for i in v.values():
        print(f'{str(i):<15}', end='')
    print()
print('=-'*40)
