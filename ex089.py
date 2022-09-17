''''crie um programa que leia nome e duas notaas de vários alunos e gaurde tudo em uma lista compostar. no final, mostre um boletim contendo a média
de cada  um e permita que o usuário possa mostrar as notas de cada aluno individualmente'''
aglomerado = []
informacoes = []
continuar = 's'
media = 0
while True:
    informacoes.append(str(input('Digite um nome: ')))
    informacoes.append(float(input('Digite a primeira nota: ')))
    informacoes.append(float(input('Digite a segunda nota: ')))
    aglomerado.append(informacoes[:])
    informacoes.clear()
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        print('Opção Inválida! por gentileza digite apenas S ou N para conmtinuar!')
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'{"ID":<4}{"NOME":<10}{"MÉDIA":8>}')
for i, p in enumerate(aglomerado):
    media = (aglomerado[i][1] + aglomerado[i][2]) / 2
    print(f'{i:<4}{p[0]:<10}{media:>5}')
while True:
    opcao = int(input('Qual aluno deseja ver? (999 para parar): '))
    if opcao == 999:
        break
    print('##' * 20)
    print(f'O aluno selecionado foi: {aglomerado[opcao][0]}')
    print(f'Suas notas são: {aglomerado[opcao][1]:.1f} e {aglomerado[opcao][2]:.1f}')
    print('##' * 20)








