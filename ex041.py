#a confederação nacional de natação precisa de um programa que leia o anscimento de um atleta e mostre sua
#categoria de acordo com a idade:
#-até 9 anos: mirim
#até 14 anos: infantil
#até 19 anos: junior
#até 20 anos sênior
#acima: master

from datetime import date
ano = int(input('Digite sua ano de seu nascimento: '))
anoat = date.today().year
anott = anoat - ano

if anott <=9:
    print(f'Você está localizado na categoria MIRIM por ter {anott} anos!')
elif anott > 9 and anott <=14:
    print(f'Você está localizado na categoria INFANTIL por ter {anott} anos!')
elif anott > 14 and anott <=19:
    print(f'Você está localizado na categoria JUNIOR por ter {anott} anos!')
elif anott == 20:
    print(f'Você está localizado na categoria SÊNIOR por ter {anott} anos!')
elif anott >20:
    print(f'Você está localizado na categoria MASTER por ter {anott} anos!')




