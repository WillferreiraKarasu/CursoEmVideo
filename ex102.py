'''crie um programa que tem uma função chamada fatorial() que receba dois parametros: o primeiro que indique
o número a calcular e o segundo chamado show que sera um valor lógico(opcional) indicando se será mostrado ou não na tela
o processo de cálculo fatorial'''

def fatorial(num, show=False):
    resultado = 1
    for n in range(1, num+1):
        resultado *= n
    return resultado







numero = int(input('Digite um número para saber seu fatorial: '))
print(fatorial(numero))

