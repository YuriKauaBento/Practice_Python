salario = float(input('Informe seu salário: '))

if salario <= 1250.0:
    print(f'Seu novo salário será de: {salario + salario * (15 / 100)}')
else:
    print(f'Seu novo salário será de: {salario + salario * (10 / 100)}')