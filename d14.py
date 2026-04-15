def conversor_temperatura():
    c = float(input('Informe a temperatura em C '))
    f = c * 1.8 + 32
    return print(f'A temperatura em fareheint é: {f:.1f}')


conversor_temperatura()