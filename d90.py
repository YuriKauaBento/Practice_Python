dic = {}

dic['nome'] = input('Nome: ')
dic['media'] = float(input('Média: '))
if dic['media'] > 7:
    dic['situacao'] = 'Aprovado'
elif 5 <= dic['media'] < 7:
    dic['situacao'] = 'Recuperação'
else:
    dic['situacao'] = 'Reprovado'

print('-='*40)
for n, m in dic.items():
    print(f'{n} é igual a {m}')