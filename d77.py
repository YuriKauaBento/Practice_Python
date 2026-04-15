palavras = ('aprender', 'gratis', 'milimetro',
            'cesio', 'uranio', 'bomba', 'camelo')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')