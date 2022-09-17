#faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis.

txt = input('Digite qualquer coisa: ')
print(f'é alfanumerico?: {txt.isalnum()}')
print(f'é alfabeto?: {txt.isalpha()}')
print(f'é tudo em minúsculo? {txt.islower()}')
print(f'é tudo em maiusculo? {txt.isnumeric()}')