from datetime import datetime
data = datetime.now().year

dados = {}
dados['nome'] = input('Nome: ')
nasc = int(input('Ano de nascmiento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de tabalho (0 para não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

#idade = data - dados['an']

print('=-'*30)
for i,j in dados.items():
    print(f'{i} tem o valor de {j}')