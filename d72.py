cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
pos = int(input('Digite um número de 0 até vinte '))

while pos > 20 or pos < 0:
    pos = int(input('Número inválido! Digite um número de 0 até vinte '))

print(f'{pos} por extenso é {cont[pos]}')
    