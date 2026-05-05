def leia_int():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except ValueError:
            print('\033[0;31mErro! Por favor, digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mErro! Entrada de dados interrompida pelo usuário.\033[m]')
            return 0
        else:
            return n


def leia_float():
    while True:
        try:
            n = float(input('Digite um número real: '))
        except TypeError:
            print('\033[0;31mErro! Por favor, digite um número real válido\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mErro! Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


print(f'O valor inteiro digitado foi {leia_int()} e o real foi {leia_float()}')