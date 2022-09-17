#faça um programa que  leia o peso de cinco pessoas.
#No final mostre qual foi o maior e o menor peso lidos.

peso = []
for pess in range(1,3):
    peso.append(float(input(f'Digite o peso da {pess}ª pessoa: ')))
print(f'O maior da lista foi{max(peso)} e o menor foi {min(peso)}')






