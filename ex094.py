'''crie um programa que leia nome, sexo e idade de várias pessoas, guardadno os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final mostre:
a) quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) yma lista com todas as pessoas com idade acima da média'''
aglomerado = list()
mulheres = dict()
pessoa = dict()
cont = 's'
soma = 0
while True:
    pessoa['nome'] = str(input('Qual seu nome? '))
    pessoa['sexo'] = str(input('Qual seu Sexo? [M/F] ')).upper().strip()
    while pessoa['sexo'] not in 'MmFf':
        pessoa['sexo'] = str(input('Opção inválida, qual seu sexo? [M/F] '))
    pessoa['idade'] = int(input('Qual sua idade? '))
    soma += pessoa['idade']
    aglomerado.append(pessoa.copy())
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while cont not in 'SsNn':
        cont = str(input('Opção inválida!, deseja continuar? [S/N] ')).upper().strip()
    if cont == 'N':
        break
print(f'Ao total foram cadastradas {len(aglomerado)} pessoas! ')
print(f'A media de idade entre as pessoas é {soma / len(aglomerado):.2f}.')
print('AS mulheres cadastradas são: ')
for c in aglomerado:
    if c['sexo'] in 'Ff':
        print(f'{c["nome"]}', end=' ')
    print()
print(f'As pessoas com idade acima da média são: ')
for c in aglomerado:
    if c['idade'] >= soma/len(aglomerado):
        print(f'{c["nome"]} com {c["idade"]} anos.')






