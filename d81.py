"""lista = []
c = 0
 
while True:
    item = int(input('Digite um número: '))
    lista.append(item)
    c += 1
    op = input('Quer continuar? [S]/[N]')
    while op.strip().upper() not in 'SN':
        op = input('Opção inválida [S]/[N]')
    if op.strip().upper() == 'N':
        print('Programa encerrado!')
        break

print(lista)
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('o valor 5 esta na lista')
else:
    print('O valor 5 não está na lista')"""

#resposta do professor
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    op = input('Quer continuar? [S/N]')
    if op in 'Nn':
        break

print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')