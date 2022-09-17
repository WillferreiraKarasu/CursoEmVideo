'''refaça o desafio 051 lendo o primeiro termo e a razão de uma PA.
mostrando os 10 primeiros termos da progressão utilizando WHILE'''

num = int(input('Digite a Termo: '))
raz = int(input('Digite o Razão: '))
termo = num
count = 1
while count != 10:
    print(f'{termo}', end=' ')
    termo += raz
    count += 1
print('Finalizado.')