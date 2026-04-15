mais18 = homem = mulhermenos20 = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    print('-' * 20)
    sexo = ''
    while sexo not in 'MF':
        sexo = input('Sexo: [M]/[F] ').strip().upper()[0]
        print('-' * 20)
#    if sexo not in 'MF':
#        print('Sexo inválido')
#       continue
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulhermenos20 =+ 1
    
    if idade >= 18:
        mais18 += 1

    op = ''
    while op not in 'SN':
        op = input('Quer continuar? [S]/[N] ').strip().upper()[0]
    if op == 'N':
        break
#    op = input('Quer continuar? [S]/[N] ').strip().upper()[0]
#    print('-' * 20)
#    if op not in 'SN':
#        print('Opção inválida!')
#        print('-' * 20)
#        break
#    elif op == 'N':
#        break
#    else:
#        continue

print(f"""Total de pessoas com mais de 18 anos: {mais18}
Total de homens cadastrados: {homem}
Total de mulheres com menos de 20 anos: {mulhermenos20}
""")
    