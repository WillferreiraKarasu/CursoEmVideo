while True:
    n = int(input('Digite um número que deseja saber a tabuada(número negativo para parar): '))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n * c}')
print('Até a próxima!')

'''faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
usuário, o programa será interrompido quando o número solicitado for negativo'''

