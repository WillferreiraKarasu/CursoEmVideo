'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depoois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário incluindo o total de gols feitos durante o campeonato'''

jogador = dict()
gol = 0
somagols = 0
jogador['nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(partidas):
    gol = int(input(f'Gols no jogo {c + 1}: '))
    jogador[f'partida{c + 1}'] = gol
    somagols += gol
print('=#' * 30)
print('Aproveitamento do jogador:')
for c in range(partidas):
    print(f'Na partida: {c + 1}, {jogador["nome"]} fez {jogador[f"partida{c + 1}"]}')
print(f'Total de gols: {somagols}')
print(jogador)
