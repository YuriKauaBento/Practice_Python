def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.
    param n: Valor a ser calculado.
    param show: (opcional) Mostrar ou nao a conta.
    return: Resultado do fatorial.
    """
    fati = 1
    for i in range(n, 0, -1):
        if show == True:
            print(f'{i}', end='')
            if i > 1:
                print(' X ', end='')
            else:
                print(f' = ', end='')
        fati *= i
    return fati

        
print(fatorial(5, True))
help(fatorial)