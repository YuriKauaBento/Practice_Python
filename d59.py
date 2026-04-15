a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
opcao = 0

while opcao != 5:
    opcao = int(input("""O que você deseja que o computador faça?
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa
"""))
    if opcao == 1:
        print(f'A soma de {a} e {b} é {a + b}')
    elif opcao == 2:
        print(f'A multiplicação de {a} e {b} é {a * b}')
    elif opcao == 3:
        if a > b:
            print(f'{a} é maior que {b}')
        else:
            print(f'{b} é maior que {a}')
    elif opcao == 4:
        a = int(input('Digite um número: '))
        b = int(input('Digite outro número: '))
    elif opcao == 5:
        print('Fim do programa')
    else:
        print('Opção inválida')
    
    print('=-=' * 10)