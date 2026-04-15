import random

numero = random.radint(1, 5)
palpite = int(input('Digite um número de 1 à 5: '))

if palpite != int:
    print('Digite um NÚMERO de 1 à 5')
elif palpite > 5 or palpite < 1:
    print('O número deve estar entre 1 e 5!')
elif palpite == numero:
    print(f'Parabéns! Você acertou! o número sorteado foi{numero}')
else:
    print('Você errou!')