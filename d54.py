from datetime import date
hj = date.today().year
maior = 0
menor = 0

for i in range(1, 8):
    ano = int(input('Informe seu ano de nascimento: '))
    idade = hj - ano
    if idade > 18:
        maior += 1
    else:
        menor += 1
    
print(f'Há {maior} maiores de idade no grupo')
print(f'Há {menor} menores de idade no grupo')