'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futyebol'''
'''na ordem de colocação, depois mostre: '''
'''A) apenas os 5 primeiros colocados'''
'''B) os ultimos 4 colocados da tabela'''
'''C) Uma lista com os times em ordem alfabética'''
'''D) em que posição da tabela está o time da CHAPECOENSE'''

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Bragantino', 'Fortaleza', 'Fluminense', 'América-MG',
         'Ceara-SC', 'Internacional', 'Santos', 'São Paulo', 'Atlético-GO', 'Juventude', 'Cuiabá', 'Athletico-PR',
         'Bahia', 'Grêmio', 'Sport Recife', 'Chapecoense')
print(f'Os cinco primeiros colocados são{times[0:5]}')
print(f'Os quatro últimos colocados são{times[-4:]}')
print(f'{sorted(times)}')
print(f'A chapecoense está no lugar: {times.index("Chapecoense") + 1}')