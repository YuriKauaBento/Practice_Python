"""from random import randint

par = impar = False
v = 0

while True:
    opcao = input('escolha entre par ou impar: [P]/[I] ').strip().upper()[0]
    print('=-=' * 20)
    if opcao not in 'PI':
        print('Opção incorreta! digite novamente')
        print('=-=' * 20)
        continue
    n = int(input('Digite um número de 0 à 10: '))
    np = randint(0, 10)
    if n > 10:
        print('Por favor digite um número de 0 até 10: ')
        print('=-=' * 20)
        continue
    else:
        if (n + np) % 2 == 0:
            par = True
            impar = False
        elif (n + np) % 2 != 0:
            par = False
            impar = True

    if par == True and opcao == 'P':
        print(f'Parabéns! o número escolhido pelo pc foi {np}, e a some entre os dois é {n + np}')
        print('=-=' * 20)
        v += 1
  
    elif impar == True and opcao == 'I':
        print(f'Parabéns! o número escolhido pelo pc foi {np}, e a some entre os dois é {n + np}')
        print('=-=' * 20)
        v +=1

    else:
        print('Perdeu!')
        print('=-=' * 20)
        break
        
print(f'Parabéns! Você venceu a máquina {v} vezes')"""

from random import randint
v = 0
while True:
    n = int(input('Digite um número de 0 à 10: '))
    np = randint(0, 10)
    total = n + np
    opcao = ''
    while opcao not in 'IP':
        opcao = input('Impar ou par? [I]/[P] ').strip().upper()[0]
    if opcao == 'P':
        if total % 2 == 0:
            print(f'Parabéns! o número escolhido pelo pc foi {np}, e a some entre os dois é {n + np}')
            v +=1 
        else:
            print('voce perdeu')
        break
    if opcao == 'I':
        if total % 2 != 0:
            print('voce perdeu')
            v +=1 
        else:
            print(f'Parabéns! o número escolhido pelo pc foi {np}, e a some entre os dois é {n + np}')
        break