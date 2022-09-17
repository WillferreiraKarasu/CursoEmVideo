

n = 0
ca = 0
cr = 0
while n != 3:
    n = int(input('opção: 1 - pegou 2 - não pegou 3 - parar: '))
    if n == 1:
        cr +=1
        ca += 1
        print(f'Total de runs {cr}, total de Ayas {ca}')
    elif n ==2:
        cr += 1
        print(f'Total de runs {cr}, total de Ayas {ca}')
    elif n == 3:
        print('Finalizando...')
print(f'Total de runs {cr}, total de Ayas {ca}')