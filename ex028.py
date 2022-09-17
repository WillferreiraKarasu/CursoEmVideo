#Escreva um programa que faça o compuntador pensar em um número inteiro entre 0 e 5 e peça para que o usuário tente descobrir
#qual foi o número escolhido pelo computador.
#computador deve dizer se usuário venceu ou perdeu


from random import randint

n = int(input('Digite um número de 0 a 5: '))
n2 = randint(0, 5)
if n == n2:
    print(f'Parabéns você acertou! eu pensei em {n2}')
else:
    print(f'Errrrrooooooooouuuuuuu eu pensei em {n2}')
