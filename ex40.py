#crie um programa que leia duas notas de umn aluno e calcule sua média, mostranod uma mensagem no final de acordo
#com a media atingida:
#Media abaixo de 5.0 reprovado.
#media entre 5.0 e 6.9 recuperação.
#media 7.0 aprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n2 + n1) / 2

if med < 5.0:
    print(f'Você foi reprovado pois sua nota foi {med:.2f}, que é menor do que o aceitavel de 7.0!')
elif med > 5.0 and med < 6.9:
    print(f'Você está de recuperação pois sua nota foi {med:.2f}, que é menor do que a aceitavel para passar (7.0)')
else:
    print('Parabéns! você foi aprovado!!!')