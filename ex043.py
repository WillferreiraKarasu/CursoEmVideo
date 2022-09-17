#deselvolva uma lógica que leia o peso e a altura de uma epssoa, calcule seu IMC e mostre seu status.
#de acordo com a tabela abaixo:
#abaixo de 18.5: abaixo do peso
#entre 18.5 e 25: peso ideal
#25 té 30: sobrepreso
#30 até 40: obesidade
#acima de 40 obesidade mórbida


peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura**2

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc<25:
    print('Você está no peso ideal!')
elif imc >= 25 and imc <30:
    print('Você está com sobrepeso!')
elif imc >=30 and imc <40:
    print('Você está com obesidade! ')
else:
    print('Você está com obesidade Morbida, Baleia!')
