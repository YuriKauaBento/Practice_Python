from time import sleep


def linha(l=50):
    return '-' * l


def cabecalho(txt):
        print(linha())
        print(f'{txt}'.center(50))
        print(linha())


def menu(lista):
    while True:
        cabecalho('MENU PRINCIPAL')
        c = 1
        for item in lista:
            print(f'\033[33m{c}-\033[0m \033[34m{item}\033[m')
            c+=1
        escolha = opcao()
        if escolha == 0:
            print(linha())
            print('Saindo... Até logo!'.center(50))
            print(linha())
            break
        return escolha


def opcao():
    while True:
        try:
            opcao = int(input('\033[32mSua opção: \033[m'))
            if 1 <= opcao <= 3:
                if opcao == 3:
                    return 0
                sleep(2)
                return opcao
            else:
                print('\033[0;31mERRO! Por favor, digite uma opção válida.\033[m')
                sleep(2)
            
        except ValueError:
            print('\033[0;31mERRO! Por favor, digite uma opção válida.\033[m')
            sleep(2)
        except KeyboardInterrupt:
            print('\033[0;31mERRO! O usuário interrompeu o programa.\033[m')
            return 0
    

