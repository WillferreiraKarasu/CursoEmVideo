'''Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a função input() do python
só que fazendo a validação para aceitar apenas um valor número
ex:
n = leiaint('digite uym numero )'''

def leiaInt(num):
    while True:
        numero = str(input(num))
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            print('Erro, digite um número válido: ')
    return numero
n = leiaInt('Digite um número: ')
print(f'O valor digitado foi: {n}')
''


