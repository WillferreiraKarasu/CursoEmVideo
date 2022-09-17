#desenvolva um sistema que pergunte  a distancia de uma viagem em KM.
#calcule o preço da passagem cobrando 0,50 por KM para viagens até 200KM.
#acima disso o valor fica em 0,45.

km = int(input('Qual a distância da viagem em KM?: '))
valor = float()

if km <= 200:
    valor = 0.50 * km
    print(f'Sua viagem ficou em R${valor:.2f}')
else:
    valor = 0.45 * km
    print(f'Sua viagem ficou em R$ {valor:.2f}')

