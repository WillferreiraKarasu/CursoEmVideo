#escreva um programa que leia um número inteiro para qualquer e peça para o usuárion escolher qual a base de conversão
# 1 para binário, 2 para Octal e 3 para hexadecimal

nm = int(input('Digite um número: '))
md = int(input('Para qual deseja converter? útilize número de 1 a 3 para escolher: \n'
               '1 - Converter para binário\n'
               '2 - Converter para Octal\n'
               '3 - Converter para Hexadecimal \n'
               ''))
if md == 1:
    print(f'O número {nm} em binário fica: {bin(nm)}')
elif md == 2:
    print(f'O valor do número {nm} em octal fica {oct(nm)}')
elif md == 3:
    print(f'O valor do número {nm} em hexadecimal fica {hex(nm)}')
else:
    print(f'Número não reconhecido, por favor digite novamente uma opção de 1 a 3')
