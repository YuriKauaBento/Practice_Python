from random import randint
from time import sleep
numeros = []


def sorteia():
    print('=-'*40)
    print('Sorteando números: ', end='')
    for i in range(0, 5):
        n = randint(0, 10)
        numeros.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')
    print('=-'*40)


def soma_par():
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos valores pares da lista {numeros} é {soma}')
    print('=-'*40)


sorteia()
soma_par()