'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte'''
'''Seu programa devera ler um número pelo teclado entre 0 e 20 e mostra-lo por extenso'''

tupula = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um número de 0 a 20: '))
while numero >20:
    numero = int(input('Número inválido, digite novamente: '))
print(f'O número escolhido foi {tupula[numero]}')







