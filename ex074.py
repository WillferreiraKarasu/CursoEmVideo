'''Crie um  programa que vai gerar cinco números aleatórios e colocar em uma tupla.'''
'''depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla'''

from random import randint
num = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Todos os números: {num}')
print(f'O maior foi: {max(num)}')
print(f'O menor foi: {min(num)}')


