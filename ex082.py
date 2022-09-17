'''Crie um programa que leia vários números e coloque em uma lista
Depois disso, crie duas listas extras, que vão conter apenas os valores pares e os valores impares digitados
ao final mostre o conteúdo das tres listas geradas.'''
valores = []
pares = []
impares = []
num = 0
resp = ' '
while True:
    num= int(input('Digite um número: '))
    valores.append(num)
    if num % 2 ==0:
        pares.append(num)
    else:
        impares.append(num)
    resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()
    while resp not in 'SN':
        resp = str(input('Opção Inválida!, digite novamente[S ou N]: ')).upper()
    if resp == 'N':
        break
valores.sort()
pares.sort()
impares.sort()
print(f'Todos os valores em ordem crescente: {valores}')
print(f'Todos os valortes pares em ordem crescente: {pares}')
print(f'Todos os valores impares em ordem crescente: {impares}')

