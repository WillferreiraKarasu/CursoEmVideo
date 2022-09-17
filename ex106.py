'''faça um mini-sistema que utilize o interactive help do python. o usuário vai digitar o comando e o
manual vai aparecer. quando o usuário digitar a palavra FIM, o programa se encerra'''

def funcoes(valor):
    help(valor)

while True:
    resp = str(input('Digite o nome da função que deseja saber: [FIM] Para encerrar: '))
    if resp.upper == 'FIM':
        break
    else:
        funcoes(resp)

