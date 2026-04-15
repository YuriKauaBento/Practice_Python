from math import pow
cateto1 = int(input('Informe o comprimeto do cateto oposto '))
cateto2 = int(input('Informe o comprimento do cateto adjacente '))
print(f'A hipotenusa é {pow(cateto1, 2) + pow(cateto2, 2)}')