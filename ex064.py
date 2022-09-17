'''crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999 que é a condição de parada.
No final mostre quandos números foram digitados e qual foi a soma entre eles desconsiderando a flag'''

from time import sleep
print('Bem vindo ao somador de números, digite qualquer número e quando quiser parar digite 999')
n = int(input('Digite um número: '))
som = c = 0
while n != 999:
    som += n
    c += 1
    n = int(input('Digite mais um número: '))
print('Finalizando...')
sleep(0.9)
print(f'O total foi de {c} números e a soma deles foi de: {som} ')