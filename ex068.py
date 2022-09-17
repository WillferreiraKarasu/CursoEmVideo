'''Faça um programa que jogue par ou impar com o computador.
O jogo só será interrompido quando o jogador perder, mostrtando o total de vitorias consecutivas que ele
conquistou no final do jogo.'''

from random import randint
c = computador = 0
while True:
    num = int(input('Digite um número de 1 a 10: '))
    computador = randint(1, 10)
    soma = num + computador
    opc = ' '
    while opc not in 'PI':
        opc = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0]
    if opc == 'P':
        if soma % 2 == 0:
            c += 1
            print('Você Venceu, vamos jogar novamente!')
        else:
            break
    elif opc == 'I':
        if soma % 2 != 0:
            c += 1
            print('Você venceu, vamos jogar novamente!')
        else:
            break
print('Você perdeu!!')
print(f'O computador escolheu {computador} e você {num}, logo a soma entre os dois dá {soma}')
print(f'Número de vitórias consecutivas {c}')