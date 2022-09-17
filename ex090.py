'''faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário, no final mostre
o conteúdo da estrutura na tela'''


aluno = {}
aluno['nome'] = str(input('Digite o nome do Aluno: '))
aluno['nota'] = float(input('Digite a nota do Aluno: '))
if aluno['Nota'] <= 6.9:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Aprovado'
print(f'O aluno {aluno["nome"]} tirou {aluno["nota"]} e está: {aluno["situação"]}')
