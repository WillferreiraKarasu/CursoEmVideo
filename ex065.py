'''crie um programa que leia vários números inteiros pelo teclado.
Nof inal da execução mostre a média entre todos os valores.
Qual foi o maior e o menor.
O programa deve perguntar se ele quer continuar a digitar sim ou não'''
from time import sleep
n = int(input('Digite um número: '))
m = c = s = 0
maior = menor = n
quest = 'S'
while quest not in 'N':
    c += 1
    s += n
    m = s / c
    quest = str(input('Deseja adicionar outro número? [S/N]: ')).upper().strip()[0]
    if quest == 'S':
        n = int(input('Digite um novo número: '))
        if n > maior:
            maior = n
        else:
            menor = n
print('Contabilizando...')
sleep(0.9)
print(f'A soma total foi de {s}, a quantidade de idades foi {c}, a média entre as idades é {m}')
print(f'A Maior idade foi {maior} e a menor idade foi {menor}')
