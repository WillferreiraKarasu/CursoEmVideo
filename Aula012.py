nome = str(input('Qual seu nome ?: '))
if nome == 'William':
    print('Que nome Lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular!')
else:
    print(f'Seu nome {nome} é bem comum!')
print(f'Seja bem vindo, {nome}!')