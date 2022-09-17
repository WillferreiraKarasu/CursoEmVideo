#crie um programa que faça o computador jogar jokenpo com você.
from random import randint
vc = int(input('[ 1 ] Pedra \n'
               '[ 2 ] Papel \n'
               '[ 3 ] Tesoura \n'))
ia = randint(1,3)

if ia == vc:
    print('Ninguém ganhou!')
elif vc == 1 and ia == 2:
    print('Eu escolhi PAPEL!\n'
          'Ganhei!!!! Fácil\n')
elif vc == 2 and  ia == 3:
    print('Eu escolhi TESOURA\n'
          'Ganhei!!!! Fácil')
elif vc == 3 and ia == 1:
    print('Eu escolhi PEDRA\n'
          'Ganhei!!!! Fácil')
elif vc == 1 and ia ==3:
    print('Eu escolhi TESOURA'
          'Você ganhou!!, está roubando ?!')
elif vc == 2 and ia == 1:
    print('Eu escolhi PEDRA\n'
          'Você ganhou!!, está roubando ?!')
elif vc == 3 and ia == 2:
    print('Eu escolhi PAPEL\n'
          'Você ganhou!!, está roubando ?!')
else:
    print('Opção Inválida')


