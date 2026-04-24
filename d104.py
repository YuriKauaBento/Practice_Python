def leia_int(msg, n=None):
    """
        Lê uma entrada para aceitar apenas variáveis int.
        :param msg: Mensagem que aparecerá no input.
        :param n: Variável que armazena o valor da entrada.
        :return: Número inserido.
    """
    while True:
        n = input(msg)
        if n.isdigit() == True:
                break
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
    return n

    
n = leia_int('Digite um número: ')
print(f'Você acabou de digitar {n}')