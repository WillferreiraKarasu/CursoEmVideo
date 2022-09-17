'''faça um programa que tenha uma função chamada ficha() , que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou
O progrma deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente'''


def ficha(n='desconhecido',g = 0):
    return f'O jogador {n} possui {g} gols'
nome = str(input('Nome do jogador: '))
gols = str(input('Quantidade de gols: '))
if nome.strip() == '':
    nome = '<desconhecido>'
if gols.isalnum():
    gols = int(gols)
else:
    gols = 0
print(ficha(nome, gols))