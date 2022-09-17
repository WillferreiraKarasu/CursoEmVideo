'''faça um programa que leia 5 valores e guarde em uma lista no final mostre qual foi o maior, qual foi o menor
e suas respectivas posições'''

valores = []
menor = 0
maior = 0
posiçãomenor = []
posiçãomaior = []
for c in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    if c == 0 or valores[c] < menor:
        menor = valores[c]
    if valores[c] > maior:
        maior = valores[c]
print(f'O menor valor digitado foi {menor} nas posições:', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}', end=', ')
print(f'\nO maior valor digitado foi {maior} nas posições: ', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}', end=', ')




