menorproduto = ' '
soma = cntprdt = contador = menorvalor = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: R$'))
    soma += valor
    if valor > 1000:
        cntprdt += 1
    if contador == 0 or valor < menorvalor:
        menorvalor = valor
        menorproduto = produto
    contador += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        print('Finalizando..')
        break
print(f'O valor gasto foi de R${soma:.2f}')
print(f'Ao total teve {cntprdt} produtos acima de R$1.000')
print(f'O produto de menor valor foi {menorproduto} no valor de R${menorvalor:.2f}')

'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguintar se o usuário
 vai continuar, no final mostre:
 a) Quan é o total gasto na compra
 b) quantos produtos custam mais de R$1000
 c) qual nome do produto mais barato'''






