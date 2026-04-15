frase = input('Digite uma frase: ')
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]

if frase == inverso:
    print(f'{frase}  {inverso}')
    print('A frase é um palindromo')
else:
    print(f'{frase}  {inverso}')
    print('A frase não é um palindromo')