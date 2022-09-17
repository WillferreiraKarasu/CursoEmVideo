#faça um programa que leia três números, e mostra qual é o maior e qual é o menor.

n1 = int(input('Digite o Primeiro número: '))
n2 = int(input('Digite o Segundo número: '))
n3 = int(input('Digite o Terceiro número: '))
#maior
if n1 > n2 and n1 > n3:
    print(f'O número {n1} é o maior de todos')
if n2 > n1 and n2 > n3:
    print(f'O número {n2} é o maior de todos')
if n3 > n1 and n3 > n2:
    print(f'O número {n3} é o maior de todos')
#menor
if n1 < n2 and n1 < n3:
    print(f'O número {n1} é o Menor de todos')
if n2 < n1 and n2 < n3:
    print(f'O número {n2} é o Menor de todos')
if n3 < n1 and n3 < n2:
    print(f'O número {n3} é o Menor de todos')

