#escreva umk programa que pergunte o salário de um funcionário e calcule se aumento
#acima de 1.250,00 calcule um aumento de 10%
#abaixo disso 15%
sal = float(input('Digite seu salário sem pontuação: '))
newsal = float
if sal >= 1250:
    newsal = (sal * 10) / 100 + sal
    print(f'Seu salário é de R${sal:.2f}, por conta disso seu aumento é de 10% totalizando R$ {newsal:.2f}')
else:
    newsal = (sal * 15) / 100 + sal
    print(f'Seu salário é R${sal:.2f} por conta disso seu aumento é de 15% totalizando R${newsal:.2f}')