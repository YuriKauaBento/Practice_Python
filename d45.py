from random import randint

itens = ['Pedra', 'Papel', 'Tesoura']
comp = randint(0, 2)
print('''Opções
      [0] Pedra
      [1] Papel
      [2] Tesoura
''')
jog = int(input('Escolha uma opção: '))
print('-=' * 11)
print(f'O computador jogou {itens[comp]}')
print(f'Você jogou {itens[jog]}')
print('-=' * 11)

if comp == 0:
    if jog == 0:
        print('Empate')
    elif jog == 1:
        print('Você ganhou')
    else:
        print('Você perdeu')
elif comp == 1:
    if jog == 0:
        print('Você perdeu')
    elif jog == 1:
        print('Empate')
    else:
        print('Você ganhou')
elif comp == 2:
    if jog == 0:
        print('Você ganhou')
    elif jog == 1:
        print('Você perdeu')
    else:
        print('empate')


