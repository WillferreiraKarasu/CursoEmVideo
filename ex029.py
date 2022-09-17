#escreva um prgrama que leia a velocidade de um carro.
#se ele ultrapassar 80KM/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar 7,00 por cada KM acima do limite.

vel = float(input('Qual a velocidade?: '))
mlt = (vel - 80) * 7
if vel >80:
    print(f'Você está acima da velocidade, por isso foi multado \n'
    f'A velocidade permitida é de 80Km/H por isso o valor da sua multa fica em R${mlt:.2f}, sendo R$7,00 por KM Excedido' )
else:
    print('Você está na velocidade permitida, continue assim!')

