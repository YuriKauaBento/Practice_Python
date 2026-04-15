termos = int(input('quantos termos deseja exibir? '))
f = 0
f2 = 1
c = 3
print(f'{f} -> {f2}', end=' ')

while c <= termos:
    f3 = f2 + f
    print(f'-> {f3}', end=' ')
    f = f2
    f2 = f3
    c += 1