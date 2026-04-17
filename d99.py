from time import sleep


def maior(*n):
    cont = m = 0
    print('=-'*40)
    print('Analisando valores passados...')
    for v in n:
        print(f'{v} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            m = v
        else:
            if v > m:
                m = v
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor informado foi: {m}')


maior(10, 3, 15, 3, 0)
maior(3, 2, 1)
maior()