'''Faça um programa que leia nome e peso de várias pessaos guardadno tudo em uma lista'''
'''no final mostre: '''
'''a) quantas pessoas foram cadastradas
b) uma listagem com as pessoas mais pesadas
c) uma listagem com as pessoas mais leves'''

conjunto = list()
pessoa = list()
contador = 0
maispesados = list()
maisleves = list()
resp = ''
while True:
    pessoa.append(str(input('Digite seu nome: ')))
    pessoa.append(int(input('Digite seu peso: ')))
    contador += 1
    conjunto.append(pessoa[:])
    if pessoa[1] >= 89:
        maispesados.append(pessoa[:])
    elif pessoa[1] <= 70:
        maisleves.append([pessoa[:]])
    resp = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Opção Inválida, por favor digite novamente[S ou N]: ')).upper().strip()[0]
    if resp in 'N':
        break
    pessoa.clear()
print(f'Ao total foram adicionadas {contador} pessoas.')
print(f'As pessoas mais pesadas foram: ', end=' ')
for i in maispesados:
    print(f'{i[0]}', end='..')
print(f'\nAs pessoas mais leves são: ', end='')
for i in maisleves:
    print(f'{1[0]}', end='..')



