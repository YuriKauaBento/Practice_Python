def area(larg, comp):
    ar = larg * comp
    print (f'A área de um terreno {larg} X {comp} é de {ar}')

lar = float(input('Largura(m): '))
com = float(input('Comprimento(m): '))

area(lar, com)