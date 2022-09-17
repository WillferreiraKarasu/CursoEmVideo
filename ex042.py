#refaça o desafio 035 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo sera formado:
#equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: Todos os lados diferentes

ld1 = float(input('Informe o primeiro lado: '))
ld2 = float(input('Informe o terceiro lado: '))
ld3 = float(input('Informe o terceiro lado: '))

if ld1 < ld2 + ld3 and ld2 < ld1 + ld3 and ld3 < ld2 + ld1:
    print('É possível formar um triangulo')
    if ld1 != ld2 and ld1 !=ld3:
        print('Seu triângulo é um ESCALENO')
    elif ld1 == ld2 and ld2 == ld3:
        print('Seu trângulo é um EQUILÁTERO')
    else:
        print('Seu triângulo é um ISÓSCELES')
else:
    print('Não é possível formar um triângulo')


