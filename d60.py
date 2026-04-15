#jeito q eu fiz
'''f = int(input('Digite um núemro para calcular seu fatorial: '))
c = f - 1
print('=-=' * 10)
print(f'O fatorial de {f} é', end=' ') 

while c > 0:
    f = f * c
    c -= 1


print(f)'''

#jeito do professor
f = int(input('Digite um número para calcular seu fatorial: '))
c = f
fat = 1
print(f'Calculando {c}!', end=' ')

while c > 0:
    print(c, end='')
    print(' x' if c > 1 else ' =', end=' ')
    fat *= c
    c -= 1

print(fat)