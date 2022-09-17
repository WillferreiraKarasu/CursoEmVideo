#crie um programa que leia o ano de nascimento de sete pessoas.
#no final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
#usar um contador
from datetime import date
maior = 0
dat = date.today().year
men = 0
for c in range(1,8):
    nasc = int(input(f'Digite {c}ª ano de nascimento: '))
    if dat >= 21:
        maior += 1
    else:
        men += 1
print(f'Foram {maior} pessoas com maioridade e {men} pessoas com menoridade.')
