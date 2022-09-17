# faça um programa que calcule a soma entre os números impares que são multiplos de 3 e que se encontram
#no intervalo de 1 até 500
soma = 0
count = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        print(c)
        soma += c
        count += 1
print('Acabou')
print(soma)
print(count)