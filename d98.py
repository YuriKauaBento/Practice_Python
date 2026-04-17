from time import sleep


def contador(a, b, c):
    print('=-'*40)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(2)
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    #for i in range(a, b, c):
    #    print(i, end=' ')
    #print(b, end=' ')
    #Como o professor fez:
    cont = a
    if a < b:
        while cont <= b:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += c
    else:
        while cont >= b:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= c
    print('FIM!')


contador(1, 10, 1)
contador(20, 0, -4)

print('Agora é a sua vez de personalizar a contagem!')
x = int(input('Início: '))
y = int(input('Fim: '))
z = int(input('Intervalo: '))

contador(x, y, z)