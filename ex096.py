'''faça um programa que tenha uyma função chamada área() qje receba as dimensões de um terreno retangular
largura e comprimento e mostre a área do terreno'''

def area(largura, comprimento):
    areatotal = largura * comprimento
    print(f'A área total é {areatotal}m²')

lar = int(input('Digite a largura: '))
comp = int(input('Digite o comprimento: '))
area(lar, comp)

