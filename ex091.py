'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. no final, coloque esse dicionário em ordem, sabendo que o vencedor tirou
o maior número do dado'''

from random import randint
from operator import itemgetter
jogadores = dict()
ranking = list()
jogadores = {'jogador1':randint(1,6), 'jogador2':randint(1,6), 'jogador3':randint(1,6), 'jogador4':randint(1,6)}
for v, k in jogadores.items():
    print(f'O {v} tirou {k} no dado.')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º ficou {v[0]} com valor {v[1]}')