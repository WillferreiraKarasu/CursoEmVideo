'''Aprimore o desafio anterior, mostrando no final:
a) a soma entre todos os valores pares digitados
b) a soma dos valores da terceira coluna
c) o maior valor da segunda linha'''

matriz = [[0,0,0], [0,0,0], [0,0,0]]
som = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um número na posição {l},{c}: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^7}]', end='')
    print()
for l in range(0,3):
    for c in range(0,3):
        som += matriz[l][c]
print(f'A soma entre todos os números é de: {som}')
print(f'O maior valor da segunda linha foi: {max(matriz[1])}')
print(f'A soma entre os valores da terceira linha foi: {sum(matriz[2])}')