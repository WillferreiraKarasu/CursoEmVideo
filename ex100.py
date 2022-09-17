'''faça um programa que tenha uma lista chamada nýmeros e duas funções chamados sorteia() e somapar().
a primeira função vai sortear 5 números e colocá-la dentro da lista e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior'''
from random import randint
from time import sleep

def sorteia(num):
    for c in range(0,5):
        num.append(randint(0,10))
    print(f'Números sorteados.. ')
    sleep(0.5)
    print(f'Os números sorteados são: ', end=' ')
    for n in num:
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)

def somapar(pares):
    soma = 0
    print(f'\nOs valores pares são: ', end=' ')
    for p in pares:
       if p % 2 == 0:
           print(f'{p}', end=' ', flush=True)
           soma += p
           sleep(0.5)
    print()
    print(f'A soma entre eles vale: {soma}')
    print('Finalizando resultados')
numeros = list()
sorteia(numeros)
somapar(numeros)
























