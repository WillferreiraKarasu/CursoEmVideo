'''Crie um programa ond eo usuário possa digitar vários valores númericos e cadastre-os em uma lista.
Caso o número já exista dentro, ele não será adicionado, no final, serão exibidos todos os valores digitados em ordem
crescente.'''
resp = ' '
valores = []
num = 0
valores.append(int(input('Digite um valor: ')))
while True:
    resp = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Opção inválida!, digite novamente [S ou N]: ')).upper().strip()
    if resp == 'N':
        break
    if resp == 'S':
        num = int(input('Digite mais um número: '))
        if num not in valores:
            valores.append(num)
        else:
            print('O valor é duplicado, não vou adicionar...')
print('Os números digitados foram:', end=' ')
for c in range(len(valores)):
    valores.sort()
    print(f'{valores[c]}', end='.. ')


