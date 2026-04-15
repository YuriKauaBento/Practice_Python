ano = int(input('Informe o ano de seu nascimento: '))
ano_a = int(input('Informe o ano atual: '))
age = ano_a - ano

if age < 1:
    print('Idade inválida')
elif age <= 9:
    print('Categoria MIRIM')
elif age <= 14:
    print('Categoria INFANTIL')
elif age <= 19:
    print('Categoria JUNIOR')
elif age == 20:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER')