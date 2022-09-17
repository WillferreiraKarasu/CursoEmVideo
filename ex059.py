'''crie um programa que leia dois valores e mostre um menu na tela
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa'''
import  time
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
com = 0
while com != 5:
    com = int(input('O que deseja fazer? \n'
                    '[1] SOMAR\n'
                    '[2] MULTIPLICAR\n'
                    '[3] VER QUAL É MAIOR\n'
                    '[4] NOVOS NÚMEROS\n'
                    '[5] SAIR DO PROGRAMA\n'))
    if com == 1:
        novovalor = v1 + v2
        print(f'A soma entre os dois é de: {novovalor}')
        novovalor = 0
        print('=' * 20)
    elif com == 2:
        novovalor = v1 * v2
        print(f'A multiplicação entre {v1} e {v2} é {novovalor}')
        novovalor = 0
        print('=' * 20)
    elif com == 3:
        if v1 > v2:
            print(f'O valor {v1} é maior que {v2}')
        elif v2 > v1:
            print(f'O valor {v2} é maior que {v1}')
        else:
            print('Ambos são iguais')
        print('=' * 20)
    elif com == 4:
        v1 = int(input('Digite um novo valor para o primeiro número: '))
        v2 = int(input('Digite um novo valor para o segundo número: '))
        print('Novos valores adicionados!')
        print('=' * 20)
    elif com == 5:
        print('Saindo do programa, aguarde um momento..')
        print('=' * 20)
    else:
        com = int(input('O valor digitado é maior do que o fornecido, por gentileza digite novamente'))
        print('=' * 20)
time.sleep(0.5)
print('Finalizado com sucesso!')

