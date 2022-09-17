'''faça um programa que tenha uma função chamada contador() que receba três parâmetros: inicio, fim e passo e realize
a contagem
seu programa tem que realize três contagems através da função criada
a) de 1 até 10 de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

def contador(ini, f, pas):
    if ini < f:
        for c in range(ini, f + 1, pas):
            print(c, end=' ')
        print()
    elif ini > f:
        for n in range(ini, f - 1, -pas):
            print(n, end=' ')
        print()
contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))

contador(inicio, fim, passo)


