'''Crie um programa que simule o funcionamento de um caixa eletronico. no inicio pergunte ao usuário qual será
o valor a ser sacado e o programa vai informar quantas cédulas de cada valor será entregues

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1'''
valor = int(input('Digite o valor a ser sacado: '))
total = valor
cedatual = 50
qtdecedulas = 0

while True:
    if total >= cedatual:
        total -= cedatual
        qtdecedulas += 1
    else:
        if qtdecedulas > 0:
            print(f'O total foi de {qtdecedulas} de R${cedatual}')
        if cedatual == 50:
            cedatual = 20
        elif cedatual == 20:
            cedatual = 10
        elif cedatual == 10:
            cedatual = 1
        qtdecedulas = 0
        if total == 0:
            break
