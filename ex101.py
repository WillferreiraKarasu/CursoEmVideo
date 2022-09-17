'''Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições'''

def voto(ano):
    from datetime import date
    anoat = date.today().year
    idade = anoat - ano
    if idade <16:
        return f'Você possui {idade} anos, sendo assim seu voto é: Proibido'
    if idade >=16 or idade <18 or idade > 65:
        return f'Você possui {idade} anos, sendo assim seu voto é: Opcional'
    else:
        return f'Você Possui {idade} anos, sendo assim seu voto é: Obrigatóro'

nascimento = int(input('Digite o ano de nascimento: '))
print(voto(nascimento))