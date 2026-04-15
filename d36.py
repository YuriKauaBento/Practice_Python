valor_c = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salário: '))
anos = float(input('Em quantos anos gostaria de parcelar o empréstimo? '))
mensal = valor_c / (anos * 12)

if mensal < salario * (30 / 100):
    print(f'Empréstimo aprovado! Valor da parcela: {mensal:.2f}')
else:
    print('Empréstimo negado!')