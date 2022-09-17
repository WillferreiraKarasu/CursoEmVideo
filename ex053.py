#crie um programa que leia uma frase qualquer e diga se ela é palindromo, desconsiderando espaços.
#frase que se le de traz pra frente e ela ainda se mantem a mesma
#ex: após a sopa de tras para frente é após a sopa.a

frase = str(input('Digite a frase sem acento: ')).upper()
nvfrase = frase.replace(' ', '') [::-1]
print(nvfrase)
if frase == nvfrase:
    print('A frase é um Palíndromo')
else:
    print('A frase não é um Palíndromo')