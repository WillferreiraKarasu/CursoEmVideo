'''aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
 do aproveitamento de cada jogador'''



'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depoois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário incluindo o total de gols feitos durante o campeonato'''

jogador = dict()
gols = list()
jogadores = list()
part = 0
cond = 'S'


while True:
    jogador.clear()
    jogador['nome'] = str(input('Qual nome do jogador?: '))
    part = int(input('Quantas partidas ele jogou?: '))
    gols.clear()
    for c in range(0, part):
        gols.append(int(input(f'Quantos gols o jogador fez na partida {c + 1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())

    tot = 0
    cond = str(input('Deseja adicionar um novo jogador? [S/N]: ')).upper().strip()[0]
    while cond not in 'SsNn':
        cond = str(input('opção inválida, digite novamente [S/N]: ')).upper().strip()[0]
    if cond == 'N':
        break
print(f'Cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print('')

for k, v in enumerate(jogadores):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
while True:
    opcao = int(input('Qual jogador deseja verificar?:  '))
    if opcao == 999:
        break
    if opcao >= len(jogadores):
        print(f'Erro! não existe jogador com o código{opcao}')
    else:
        print(f'Levantamento do jogador {jogadores[opcao]["nome"]}: ')
        for i, g in enumerate(jogadores[opcao]["gols"]):
            print(f'No jogo {i+1} fez {g} gols')







