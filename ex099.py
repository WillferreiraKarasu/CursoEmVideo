'''faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros
seu programa tem que analisar todos os valores e dizer qual deles é o maior'''
# from random import randint
#
# # def maior(m):
# #     print('Os números selecionados foram: ')
# #     print('=' * 30)
# #     for n in m:
# #         print(n, end=', ')
# #     print()
# #     print('=' * 30)
# #     print(f'Dentre eles o maior foi {max(m)}.')
# #     print('=' * 30)
# #     print(f'Ao total foram sorteados {sorteios} números')
# #
# #
# #
# # numeros = []
# # numeros = [randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100)]
# # maior(numeros)
def linha():
    print('=' * 40)
def maior(*m):
    linha()
    print(f'Números Sorteados: ')
    for c in m:
        print(f'{c}', end=', ')

    print()
    print(f'O maior foi: {max(m)}')
    print(f'Ao total foram selecionados {len(m)} números.')

maior(2, 3, 1, 5, 10, 11, 23, 42)
maior(1, 3)
maior(7, 8, 9)
maior(13, 23, 77, 1)
maior(99, 23, 14, 44, 47)





