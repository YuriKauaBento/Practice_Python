"""matriz = [[], [], []]
valor = 0

for i in range(0, 9):
    valor = int(input('Digite um número: '))
    if len(matriz[0]) < 3:
        matriz[0].append(valor)
    elif len(matriz[1]) < 3:
        matriz[1].append(valor)
    else:
        matriz[2].append(valor)

print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for e in range(0, 3):
        matriz[i][e] = int(input(f'Digite um valor para a posição {i}, {e}: '))
for i in range(0, 3):
    for e in range(0, 3):
        print(f'[{matriz[i][e]:^5}]', end='')
    print()
