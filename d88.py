from random import randint
from time import sleep

print('-'*20)
print('JOGA NA MEGA'.center(20))
print('-'*20)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(0, jogos):
    nums = []
    for n in range(0, 6):
        nums.append(randint(1, 60))
    print(f'Jogo {i+1}: {nums}')
    sleep(1)
    nums.clear
