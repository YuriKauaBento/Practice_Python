from datetime import date

ano = int(input('Informe seu ano de nascimento: '))
ano_a = date.today().year
age = ano_a - ano

if age < 18:
    print(f'Você ainda vai precisar se alistar ao serviço militar daqui a {18 - age} anos')
if age == 18:
    print('Já está na hora de se alistar ao serviço militar.')
else:
    print(f'Já passaram {age - 18} anos da hora de se alistar.')