#elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal
#e condição de pagamento.
#-A vista no dinheiro ou pix 10% de desconto
#a vista no cartão 5% de desconto
#em até 2x no cartão preço nmormal
#3x ou mais 20% de juros

valor = float(input('Qual valor da compra ? \n'))
pag = int(input('Qual a forma de pagamento? \n'
                '1 - A vista no dinheiro ou pix (10% de desconto)\n'
                '2 - A vista no cartão (5% de desconto)\n'
                '3 - em até 2x no cartão\n'
                '4 - 3x ou mais (20% de juros)\n'))
if pag == 1:
    valor = valor - (valor * 10) / 100
    print(f'Por você estar pagando em dinheiro ou pix você tem até 10% de desconto\n'
          f'O valor fica em R${valor:.2f}')
elif pag ==2:
    valor = valor - (valor * 10) / 100
    print(f'Por você estar pagando a vista em cartão seu desconto é de desconto\n'
          f'O valor fica em R${valor:.2f}')
elif pag ==3:
    valor = valor / 2
    print(f'Você está pagando em 2x no cartão, essa opção não possui desconto.\n'
          f'O valor fica em R$ {valor:.2f}')
elif pag == 4:
    valor = valor + (valor * 20) /100
    vezes = int(input('Em quantas vezes? '))
    valor = valor / vezes
    print(f'Você está pagando em 3x ou mais, essa opção possui 20% de juros no valor total.\n'
          f'Quantidade de vezes  {vezes}\n'
          f'Valor final: R${valor:.2f}')
else:
    print('Opção invalida')




