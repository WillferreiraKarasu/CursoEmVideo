'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla, no final mostre:'''
'''a) quantas vezes apareceu o valor 9'''
'''b) em que posiução foi digitado o primeiro valor 3'''
'''c) quais foram os números pares'''

tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
         int(input('Digite um número: ')))
par = 0
num = 0
nove = 0
while num < 4:
    if tupla[num] % 2 == 0:
        par += 1
    num += 1
if 3 in tupla:
    print(f'O número 3 apareceu na posição {tupla.index(3)}')
print('Os números pares são: ')
for c in range(0, 4):
    if tupla[c] % 2 ==0:
        print(f'{tupla[c]}', end=' ')
print()
print(f'O número 9 apareceu {tupla.count(9)} vezes')

