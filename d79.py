lista = []

while True:
    item = 0
    item = int(input('Digite um número: '))
    if item not in lista:
        lista.append(item)
    op = input('Quer continuar? [S/N]')
    while op.strip().upper() not in 'NS':
        op = input('Quer continuar? [S/N]')
    if op.strip().upper() == 'N':
        break

print(lista.sort())