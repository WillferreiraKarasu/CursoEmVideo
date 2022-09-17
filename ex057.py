'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores como M ou F
Caso esteja errado, peça a digitação novamente até ter um valor correto'''

sexo = str(input('Digite seu sexo: [M] ou [F] ')).upper().strip()[0]
while sexo not in 'FM':
    sexo = str(input('Opção inválida, por Gentileza selecione novamente: ')).upper().strip()[0]
print(f'Sexo {sexo} Cadastrado.')

