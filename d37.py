num = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções:
      [1] BINÁRIO
      [2] OCTAL
      [3] HEXADECIMAL''')
opcao = int(input('Escolha sua opção! '))

if opcao == 1:
    print(f'O BINÁRIO de {num} é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'O OCTAL de {num} é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'O HEXADECIMAL de {num} é igual a {hex(num)[2:]}')
else:
    print('Opção inválida!')