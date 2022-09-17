'''Escreva um programa que leia um número N inteiro e mostre na tela os 1 primeiros elementos de uma
Sequência de fibonacci'''

# '''Variavel para selecionar a quantidade de sequências'''
# qtd = int(input('Digite a quantidade de termos da sequência de fibonnaci você deseja saber: '))
#
# '''Variavel para guardar o valor de anterior, começando em 0'''
# anterior = 0
#
# '''Variavel para guardar o valor posterior, começando em 0'''
# posterior = 0
#
# '''Contador para realizar a quantidade correta de termmos selecionada pelo usuário'''
# c = 0
# '''enquanto contador for menor do que a quantidade de termos da sequência, faça:'''
# while c < qtd:
#     '''Printar o posterior para começar em zero'''
#     print(posterior)
#     '''Posterior recebe o número anterior'''
#     posterior += anterior
#     '''Anterior se torma o posterior, sendo posterior - anterior'''
#     anterior = posterior - anterior
#
#     '''Se o posterior for igual a 0 ele incrementa +1'''
#     if posterior == 0:
#         posterior += 1
#     '''Adicionamos um contador para não se tornar um loop infinito'''
#     c += 1

qtd = int(input('Digite a quantidade de termos de fibonnaci que deseja saber: '))
anterior = 0
posterior = 0
c = 0

while c < qtd:
    print(posterior)
    posterior += anterior
    anterior = posterior - anterior
    if posterior ==0:
        posterior += 1
    c += 1


















