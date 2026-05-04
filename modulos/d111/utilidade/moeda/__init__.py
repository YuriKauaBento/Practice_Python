#formatação incluída no exercício 108
def aumentar(n=0, taxa=0, m = False):
    a = n + n * (taxa / 100)
    return a if m == False else moeda(a)
#    if m == True:
#        return moeda(a)
#    else:
#        return a


def metade(n=0, m = False):
    me = n / 2
    return me if m == False else moeda(me)
#    if m == True:
#        return moeda(me)
#    else:
#        return me


def diminuir(n=0, taxa=0, m = False):
    d = n - n * (taxa / 100)
    return d if m == False else moeda(d)
#    if m == True:
#        return moeda(d)
#    else:
#        return d


def dobro(n=0, m = False):
    db = n * 2
    return db if m == False else moeda(db)
#    if m == True:
#        return moeda(db)
#    else:
#       return db


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(preco, aumento, reducao):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preço analizado: \t{moeda(preco)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de diminuição: \t{diminuir(preco, reducao, True)}')
    print('-'*40)