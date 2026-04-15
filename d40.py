n1 = float(input('Informe sua primeira nota: '))
n2 = float(input('Informe sua segunda nota: '))
media = (n1 + n2) / 2

if media > 5:
    print('Reprovado!')
elif media > 5 and media < 6.9:
    print('Recuperação!')
else:
    print('Aprovado!')