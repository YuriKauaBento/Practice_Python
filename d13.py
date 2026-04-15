def novo_salario():
    salario = float(input('Informe seu salário: '))
    aumento = salario + (salario * 15/100)
    return print(f'O seu novo salário é: {aumento}')


novo_salario()
