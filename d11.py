def medidas(largura, altura):
    area = largura * altura
    tinta = area / 2
    return print(f'A area é {area} e a quantidade de tinta em litros necessária é {tinta}')


largura = int(input('Informe a largura: '))
altura = int(input('Informe a largura: '))

medidas(largura, altura)