caro = total = precon = cont = 0
nomeb =''

while True:
    print('-' * 20)
    print('Loja')
    print('-' * 20)
    nome = input('Nome do produto: ')
    preco = float(input('Preço: '))
    cont += 1
    if cont == 1:
        precon = preco
        nomeb = nome
    elif precon > preco:
        precon = preco
        nomeb = nome
    if preco >= 1000:
        caro += 1
    total += preco
    op = ' '
    while op not in 'SN':
        op = input('Quer continuar? [S]/[N] ').strip().upper()[0]
    if op == 'N':
        break

print(f"""O total da compra foi {total}
Temos {caro} custando mais de RS 1000.00
O produto mais barato foi {nomeb} que custou R$ {precon}
""")