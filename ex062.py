'''melhores o desafio 61 perguntando para o usuário se ele quer mostrar mais alguns termos, o programa encerra quando
ele disser que quer mostrar 0 termos
quando adicionar novo termo ele continua de onde parou'''

from time import sleep
num = int(input('Digite o primeiro Termo da PA: '))
raz = int(input('Digite a razão da PA: '))
term = num
c = 1
rz = 10
while c != rz:
    print(f'{term}')
    term += raz
    c += 1
    if c == rz:
        continuar = int(input('Deseja mostrar mais quantos? '))
        if continuar == 0:
            print('Finalizando...')
        else:
            c = 1
            rz = continuar + 1
sleep(0.8)
print('Programa finalizado')




