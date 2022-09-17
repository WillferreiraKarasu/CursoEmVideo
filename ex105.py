'''faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- quantidade de notas
- a maior nota
- a menos nota
- a media
- a situação
adicione também as docstrings da função'''

def notas(*num, sit=False):
    """
    :param num: Recebe as resposta das notas
    :return: REtorna os valores de acordo com a necessidade, sendo maior, menor e media das notas
    """
    dic = {'MaiorNota':max(num),'MenorNota':min(num),'Media':sum(num) / len(num), 'QuantidadeNotas':len(num)}
    situacao = 'REPROVADO'
    if sum(num) / len(num) > 8:
        sit = True
        situacao = 'APROVADO'
    else:
        sit = False
        situacao = 'REPROVADO'
    dic['Situacao'] = situacao
    return dic
resposta = notas(8.5, 9.3, 8.2, sit=False)
print(resposta)
