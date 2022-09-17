'''Crie um programa que tenha uma tupla única com os nomes dos produtos e seus respectivos preços na sequência'''
'''No final mostre uma listagem de preços organizando os dados em forma tabular'''

tabelapreço = ('Arroz', 30.20, 'Feijão', 15.20, 'Caixa de bombom', 9.99, 'Alface', 2.99, 'Fraldinha', 20.19)

for c in range(0, len(tabelapreço)):
    if c % 2 ==0:
        print(f'{tabelapreço[c]:<20}', end=' ')
    else:
        print(f'{tabelapreço[c]:>7.2f}')
