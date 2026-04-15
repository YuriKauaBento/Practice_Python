lista = []
pares = []
impares = []

while True:
    item = int(input('Digite um número: '))
    lista.append(item)
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)
    op = input('Quer continuar? [S/N]')
    if op in 'Nn':
        break

print(f'A lista digitada foi: {lista}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')

#para adicionar os valores às listas, o professor não utilizou a estrutura if dentro do while:
"""for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
"""