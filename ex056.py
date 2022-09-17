#desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#no final do programa mostre:

#a media da idade do grupo.
#qual é o nome do homem mais velho
#quantas mulheres tem menos de 20 anos.

med = 0
cont = 0
maisvl = ''
maisvlid = 0
idades = 0
for p in range(1,5):
    idade = int(input(f'Qual idade da {p}ª pessoa? '))
    nome = str(input(f'Qual nome da {p}ª pessoa? '))
    mxh = int(input(f'É Mulher? \n'
                    f'1 - SIM\n'
                    f'2 - NÃO'))
    idades += idade
    if mxh == 1 and idade <20:
        cont += 1
    elif mxh == 2 and p == 1:
        maisvl = nome
        maisvlid = idade
    if maisvlid < idade:
        maisvlid = idade
        maisvl = nome
med = idades / p
print(f'A media de idades foi de {med}')
print(f'Existem {cont} Mulheres')
print(f'O homem mais velho é {maisvl} com {maisvlid} anos')



