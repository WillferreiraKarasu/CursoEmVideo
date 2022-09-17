#faça uma tabuada de um número que o usuário escolher usando for
tab = int(input('Digite a tabuada que deseja saber:\n'))
for c in range(1, 11):
    print(f'{tab} X {c} = {tab*c} ')
