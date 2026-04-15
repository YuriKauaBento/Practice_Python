from random import randint
from time import sleep
from operator import itemgetter

players = {'jogador1': randint(0,6), 'jogador2': randint(0,6), 'jogador3': randint(0,6), 'jogador4': randint(0,6)}

for k, v in players.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'{k} tirou {v} no dado.')
    sleep(1)
