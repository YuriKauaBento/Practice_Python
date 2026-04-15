ivelho = 0
soma = 0
media = soma / 4
velho = ''
mulher = 0
for i in range(1, 5):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo [M]/[F]: ')
    media += idade
    if i == 1 and sexo in 'Mm':
        ivelho = idade
    if ivelho < idade and sexo in 'Mm':
        ivelho = idade
        velho = nome
    if idade < 20 and sexo in 'Ff':
        mulher = mulher + 1

print(f"""A média de idades é {media}
        O mais velho é {velho}
        Há {mulher} mulheres com menos de 20 anos
""")