p = {}
pessoas = []
media = 0
mulheres = []
maior = []

while True:
    p['Nome'] = input('Nome: ')
    p['Sexo'] = input('Sexo[F/M]: ')
    while p['Sexo'] not in 'FfMm':
        print('Erro! Por favor, digite apenas M ou F.')
        p['Sexo'] = input('Sexo[F/M]: ')
    p['Idade'] = int(input('Idade: '))
    pessoas.append(p.copy())
    p.clear()
    op = input('Quer continuar? [S/N] ')
    while op not in 'NnSs':
        print('Erro! Por favor, digite apenas S ou N')
        op = input('Quer continuar? [S/N] ')
    if op in 'Nn':
        break

for i in pessoas:
    media += i['Idade']
    if i['Sexo'] in 'Ff':
        mulheres.append(i['Nome'])

media = media / len(pessoas)


print('=-'*40)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade foi de {media} anos.')
print(f'Mulheres: {mulheres}')
print('Lista de pessoas que tem idade acima da média: ')
for i in pessoas:
    if i['Idade'] > media:
        print(f'Nome = {i['Nome']}; sexo = {i['Sexo']}; idade = {i['Idade']}')
print('=-'*40)
