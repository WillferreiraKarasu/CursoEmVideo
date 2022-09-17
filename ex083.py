'''crie um programa onde um usuário digite uma expressão qualquer que use parenteses.
Seu aplicatiuvo deverá analissar se a expressão passada está com parênteses abertos e fechados na ordem correta'''
exp = input('Digite a expressão: ')
if exp.count('(') != exp.count(')'):
    print('Expressão incorreta!')
else:
    print('Expressão correta!')