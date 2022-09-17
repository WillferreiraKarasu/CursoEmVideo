cm = cf = ci = 0
while True:
    idade = int(input('Qual sua idade?: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Qual seu Sexo? [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        cm +=1
    elif sexo == 'F' and idade < 20:
        cf += 1
    if idade > 18:
        ci += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        print('Finalizando..')
        break
print(f'Ao total foram: ')
print(f'{ci} Pessoas tem +18 anos ')
print(f'{cf} São mulheres e tem menos de 20 anos ')
print(f'{cm} São homems')

'''Crie um programa que leia idade e o sexo de várias pessoas, a cada pessoa cadastrada o programa devera
perguntar se o usuário quer ou não continuar.
No final mostre:
A -> quantas pessoas tem mais de 18 anos
b -> QUantos homems foram cadastrados
c -> QUantas mulheres tem menos de 20 anos'''