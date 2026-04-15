"""lista = []
impar = []
par = []

for i in range(0, 7):
    temp = int(input('Digite um núemro: '))
    lista.append(temp)
    if temp % 2 == 0:
        par.append(temp)
    else:
        impar.append(temp)
    
print(lista)
par.sort()
impar.sort()
print(f'Impares: {impar}')
print(f'Pares: {par}')"""

num = [[], []]
valor = 0

for i in range(0, 7):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()
print(f'Impares: {num[1]}')
print(f'Pares: {num[0]}')