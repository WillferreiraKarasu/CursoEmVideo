'''Crie um programa onde o usuário possa digitar sete valores números e cadastre-os em uma lista única que mantenha
separados os valores pares e impares. no final mostre os pares e impares em ordem crescente'''

numeros = []
for c in range(0,7):
     numeros.append(int(input('Digite um número: ')))
numeros.sort()
print('Números pares: ',end=' ')
for p in numeros:
    if p % 2 ==0:
        print(f'{p}', end=' ')
print('\nNúmeros impares: ', end=' ')
for i in numeros:
    if i % 2 == 1:
        print(f'{i}', end=' ')
