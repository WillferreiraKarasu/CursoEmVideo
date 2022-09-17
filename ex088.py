'''faça um programa que ajude um jogador da mega sena a criar palpites, o programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta'''
from random import randint
from time import sleep
numeros = []
jogo = []
randomico = 0
print('='* 18, 'Bem vindo!', '=' * 18)
qtdejogo = int(input('Qual a quantidade de jogos?:  '))
print('='* 47)
for c in range(0, qtdejogo):
    for n in range(0, 6):
        randomico = randint(1, 60)
        while randomico in jogo:
            randomico = randint(1, 60)
        jogo.append(randomico)
    jogo.sort()
    numeros.append(jogo[:])
    jogo.clear()
for l in range(0, len(numeros)):
    for n in range(0, 6):
        print(f'[{numeros[l][n]:^5}]', end=' ')
    sleep(1)
    print(' ')
print('='* 18, 'Boa sorte!', '=' * 18)








