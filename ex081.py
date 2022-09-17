'''Crie um programa que leia vários números e coloque em uma lista, depois disso mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista'''

contador = 0
valores = []
resp = ' '
while True:
    valores.append(int(input('Digite um número: ')))
    contador +=1
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if resp == 'N':
        break
    while resp not in 'SsnN':
        resp = str(input('Resposta incorreta!, Deseja continuar? [S/N]: ')).upper().strip()
valores.sort(reverse=True)
print(f'A lista ordenada de números selecionados é: {valores}')
if 5 in valores:
    print(print(f'O valor 5 foi digitado.'))
else:
    print('O valor 5 não foi digitado.')
print(f'Ao total foram digitados: {contador} Números.')