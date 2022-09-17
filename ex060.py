'''faça um programa que leia um número qualquer e mostre seu fatorial
ex: 5! = 5x4x3x2x1=120'''

from math import factorial
num = int(input('Digite um número para saber seu fatorial: '))
fat = num - 1
soma = factorial(num)
print(f' O fatorial de {num}! é: ')
while fat != 0:
    print(f'{num} X {fat}', end=', ')
    num -= 1
    fat -= 1
print(f'= {soma}')



