'''Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista
Já na posição correta de inserção sem usar sort
No final mostre a lista ordenada na tela'''

valores = []
num = 0
for c in range(0,5):
    num = int(input('Digite um número: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
    else:
        posicao = 0
        while posicao < len(valores):
            if num <= valores[posicao]:
                valores.insert(posicao, num)
                break
            posicao += 1
print(f'Todos os valores em ordem: {valores}')

