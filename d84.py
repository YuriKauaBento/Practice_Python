temp = []
lista = []
maior = menor = 0

while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if maior < temp[1]:
            maior = temp[1]
        if menor > temp[1]:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear
    op = input('Quer continuar? [S/N]')
    if op in 'Nn':
        break

    print(f'Ao todo, você cadastrou {len(lista)} pessoas')
     
    for p in lista:
        if p[1] == maior:
            print(f'[{p[0]}] ', end='')
print()
print(f'O maior peso foi de {menor}KG. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f''[{p[0]}] ', end=''')