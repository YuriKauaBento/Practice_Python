a = int(input('informe o comprimento da primeira reta: '))
b = int(input('Informe o comprimento da segunda reta: '))
c = int(input('Informe o comprimento da terceira reta: '))

if a + b > c and b + c > a and c + a > b:
    print('As retas podem formar um triângulo')
else:
    print('As retas n podem formar um triângulo')