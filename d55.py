maior = 0
menor = 0

for i in range('1, 6'):
    peso = float(input('Digite seu peso: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso

print(f'O maior peso é {maior} e o menor peso é {menor}')