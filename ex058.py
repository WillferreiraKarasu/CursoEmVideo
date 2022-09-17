'''melhores o jogo do desafio 28 onde o computador vai 'pensar' em um número entre 0 e 10.
Só que agora o jogador vai tentar advinhar até acerttar, mostrando no final quantos palpites foram necessários
para vencer.'''

from random import randint
ia = randint(0,10)
vc = int(input('Digite um número de 0 a 10: '))
c = 0
while vc != ia:
    vc = int(input('Você errou!, tente novamente: '))
    c += 1
print(f'Você acertou! parabéns!! O número escolhido foi {ia}!!')
print(f'Número de palpites: {c}')

