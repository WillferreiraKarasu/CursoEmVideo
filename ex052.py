#faça um programa que leia um número inteiro e diga se ele é ou não um número primo
#numeros primos são números divididos por 1 ou por ele mesmo
num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
if cont > 2:
    print(f'O número {num} não é PRIMO')
else:
    print(f'O número {num} é PRIMO')