'''Crie um programa que tenha uma tupla com várias palavras(não usar acentos)'''
'''Depois disso você deve mostrar cada palavra quais são suas vogais'''

tupla = ('banana', 'maça', 'canela', 'repolho', 'goiaba', 'queijo')

for palavras in tupla:
    print(f'\n Na palavra {palavras.upper()} temos: ', end=' ')
    for letra in palavras:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')






