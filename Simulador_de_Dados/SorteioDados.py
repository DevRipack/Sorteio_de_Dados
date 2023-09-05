from random import randint
from time import sleep
from operator import itemgetter

count = 0
while count < 6:
        jogo = {'   jogador 1': randint(1, 12),
                '   jogador 2': randint(1, 12),
                '   jogador 3': randint(1, 12),
                '   jogador 4': randint(1, 12),
                '   jogador 5': randint(1, 12),
                '   jogador 6': randint(1, 12),
                '   jogador 7': randint(1, 12),
                '   jogador 8': randint(1, 12),
                '   jogador 9': randint(1, 12),
                '   jogador 10': randint(1, 12),
                '   jogador 11': randint(1, 12),
                '   jogador 12': randint(1, 12)}
        
        count += 1 
ranking = set(list())
print('Valores sorteados: ')
print('-=' *7,' Ranking ','-=' *8)
for key, value in jogo.items():
        print(f'{key} tirou {value} no dado.')
        sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' *17)
for i, v in enumerate(ranking):
        print(f'    {i+1}º lugar:{v[0]} com {v[1]}.')
        sleep(1)