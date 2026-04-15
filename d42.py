a = int(input('informe o comprimento da primeira reta: '))
b = int(input('Informe o comprimento da segunda reta: '))
c = int(input('Informe o comprimento da terceira reta: '))

if a + b > c and b + c > a and c + a > b:
    if a == b and a == c:
        print('O triangulo é equilatero')
    elif a == b or a == c or b == c:
        print('O triangulo é isoceles')
    else:
        print('O triangulo é escaleno')
else:
    print('As retas n podem formar um triângulo')

