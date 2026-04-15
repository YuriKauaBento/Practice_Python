preco = float(input('VALOR DAS COMPRAS: R$'))
print('''FORMAS DE PAGAMENTO:
      [1] À VISTA
      [2] À VISTA NO CARTÃO
      [3] 2X NO CARTÃO
      [4] 3X OU MAIS NO CARTÃO
''')
opcao = input('OPCAO ESCOLHIDA: ')
parcelas = input('QUANTIDADE DE PARCELAS: ')

if opcao == 1:
    print(f'Sua compra será parcelada em {parcelas}x COM DESCONTO')
    print(f'Sua compra de {preco} vai custar {preco - preco * 0.10}')
elif opcao == 2:
    print(f'Sua compra será parcelada em {parcelas}x COM DESCONTO')
    print(f'Sua compra de {preco} vai custar {preco - preco * 0.5}')
elif opcao == 3:
    print(f'Sua compra será parcelada em {parcelas}x SEM JUROS')
    print(f'Sua compra de {preco} vai custar {preco}')
elif opcao == 4:
    print(f'Sua compra será parcelada em {parcelas}x COM JUROS')
    print(f'Sua compra de {preco} vai custar {preco + preco * 0.20}')
else:
    print('Opção inválida')
