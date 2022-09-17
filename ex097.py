'''faça um programa que tenha uma função chamada escreva() que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável
ex: escreva('Olá mundo!')
saida:
----------
Olá, mundo!
----------'''

def escreva(texto):
    print('=' * len(texto))
    print()
    print(texto)
    print()
    print('=' * len(texto))


texto = str(input('Digite o texto a ser mostrado: '))
escreva(texto)




