#escreva um programa que para aprovar o empréstimo bancário para a compra de uma casa o programa vai perguntar:
#valor da casa, salário e quantos anos vai demorar para pagar.
#calcule o valor da prestação mensal, sabendo que não pode exceder 30% do salário ou empréstimo vai ser negado.


vl = float(input('Qual o valor da casa? '))
sl = float(input('Qual seu salário ? '))
months = int(input('Em quantos meses vai pagar? '))
vlpcl = vl / months
trntpc = sl * 30 / 100

if trntpc > vlpcl:
    print(f'A parcela do seu empréstimo é de R${vlpcl:.2f}, por ela ser menor ou igual a 30% do seu salário de R${sl:.2f}\n'
          f'Seu empréstimo está Aprovado!!')
else:
    print(f'Infelizmente o empréstimo foi negado pois o valor da parcela é de R${vlpcl:.2f}\n'
          f'isso ultrapassa trinta por cento do seu salário de R${sl:.2f}\n'
          f'Para ser aprovado o valor da parcela deve ser até R${trntpc:.2f}')


