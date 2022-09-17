soma = contador = 0
while True:
    numero = int(input('Digite um número (999 para finalizar): '))
    if numero == 999:
       break
    soma += numero
    contador += 1
print(f'A quantidade de números digitados foi {contador} e a soma entre eles é de: {soma}')

'''Crie um programa que leia vários números inteiros pelo teclado. o programa só para quando o usuáriop digitar 999
que é a condição de parada. no final, mostre quantos números foram digitados e qual foi a soma entrre eles
desconsiderando 999'''
