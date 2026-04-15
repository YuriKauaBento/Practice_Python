frase = input('Digite algo: ').upper()
print(f'Quantidade de letras A: {frase.count('A')}')
print(f'Primeira aparição da letra A: {frase.find('A') + 1}')
print(f'Última aparição da letra A: {frase.rfind('A') + 1}')