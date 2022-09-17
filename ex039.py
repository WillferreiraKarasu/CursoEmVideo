#faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
#-se ele ainda vai se alistar ao serviço militar.
#se é a hora de se alistar.
#se já passou do tempo de se alistar
#seu programa também devera mostrar o tempo que falta ou que passou fora do prazo.

from datetime import date

ano = int(input('Digite o ano do seu nascimento: '))
anoat = date.today().year
dif = year - anoat

if dif > 18:
    print(f'Já se passaram {dif - 18} anos do seu alistamento.')
elif dif < 18:
    print(f'Ainda falta {18 - dif} anos para o seu alistamento.')
else:
    print(f'Você possui idade correta para se alistar, vá se alistar esse ano.')


