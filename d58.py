from random import randint

comp = randint(0, 10)
player = int(input('Digite um número de 0 à 10: '))
tent = 1

while comp != player:
    if player < comp:
        player = int(input('Mais... Tente outra vez: '))
    else:
        player = int(input('Menos.. Tente outra vez: '))
    
    tent += 1

print(f'Parabéns! Você acertou após {tent} tentativas!')