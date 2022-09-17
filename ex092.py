'''Crie um programa que leia nome, ano de mascimento e carteira de trabalho e cadastre-os(com idade)m dicionário
se por acaso a CTPS for diferente de ZERO, o dicionário recebera tambémk o ano da contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar'''

from datetime import date

documentos = {}
documentos['nome'] = str(input('Qual seu nome? '))
documentos['ano'] = date.today().year - int(input(f'{documentos["nome"]}, qual ano do seu nascimento?: '))
documentos['ctps'] = int(input(f'{documentos["nome"]}, qual sua ctps?, caso não possua digite 0: '))
if documentos['ctps'] != 0:
    documentos['anocontrato'] = int(input('Qual o ano de contratação? '))
    documentos['salario'] = float(input('Qual seu salário?: '))
    documentos['aposentadoria'] = (35 - (date.today().year - documentos['anocontrato'])) + documentos["ano"]
    print('=#' * 30)
    for k, v in documentos.items():
        print(f'{k} tem o valor {v}')
elif documentos['ctps'] == 0:
    for k, v in documentos.items():
        print(f'{k} tem o valor{v}')


