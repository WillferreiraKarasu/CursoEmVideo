'''Crie um programa que crie uma matriz de dimensão 3x3 e preeencha com valores lidos pelo teclado
no final mostre a matriz na tela, com a formatação correta'''
matrizes = [[], [], []]
valores = 0
for c in range(0,9):
    valores.append(int(input(f'Digite o {c + 1}º número: ')))
    if c == 2:
        matrizes.append(valores[:])
        valores.clear()
    elif c == 5:
        matrizes.append(valores[:])
        valores.clear()
    elif c == 8:
        matrizes.append(valores[:])
        valores.clear()
for a in range(0,3):
    print(f'[{matrizes[0][a]:^7}]', end='')
print('')
for b in range(0,3):
    print(f'[{matrizes[1][b]:^7}]', end='')
print('')
for c in range(0,3):
    print(f'[{matrizes[2][c]:^7}]', end='')
