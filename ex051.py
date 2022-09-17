#desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmetica.
#no final mostre os 10 primeiros termos dessa progressão

num = int(input('Digite o primeiro número: '))
term = int(input('Digite o termo da progressão: '))
dec = num + (10 - 1) * term
for c in range(num, dec + term, term):
    print(c, end=' ')
