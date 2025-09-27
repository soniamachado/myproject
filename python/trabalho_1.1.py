import math_1
'''Desenvolver um programa em Pyhton, que solicite ao utilizador 2 valores de vírgula flutuante a seguinte análise entre esses
dois valores
Introduxir o início do intervalo
Introduzir o fim do intervalo

Quantidade de número pares
maior número par
menor número ímpar
somatório dos número pares
quantidade de números primos
média de números ímpares
maior número não primo
menor número primo
somatório de todos os números inteiros
média de todos os números inteiros'''
while True:
    valor_inicial=float(input("Introduza um valor inicial do intervalo:").replace(',','.'))
    valor_final=float(input("Introduza o último valor do intervalo:").replace(',','.'))

    #verifica a ordem dos valores
    if valor_inicial>valor_final:
        print('erro:o valor inicial deve ser menor ou igual ao valor final. Tente novamente\n')
        continue
    else:
        valor_inicial_inteiro=int(valor_inicial)
        valor_final_inteiro=int(valor_final)   
        math_1.paridade(valor_inicial_inteiro, valor_final_inteiro)
        break   
