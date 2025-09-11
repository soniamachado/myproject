# 1-implementar um programa em Pyhton que solicite ao usuario um texto e no caso de ser igual a ProgramarPyton exibe a frase "FIM"
name=input('exercicio 1-Enter your name:')
print('Your name is:', name)
print('and it has\t', len(name), '\t charachter')
#2-Desenvolver um programa em Python que solicita um valor ao utilizador e indica se o valor é par ou ímpar
valor=int(input('exercicio 1-Enter your name:'))
if valor % 2 == 0:
    print('O valor é par')
else:
    print('O valor é impar')
#4 
'''Implementar um programa em Python que solicita ao utilizador um valor numérico e faz a
seguinte avaliação:
➢ Se igual a zero escrever Valor nulo
➢ Se maior que zero escrever Valor positivo
➢ Se menor que zero escrever Valor negativo'''
numero=int(input('introduza um número'))
if numero==0:
    print('Valor nulo')
elif numero>0:
    print('Valor positivo')
else :
    print('valor negativo')

#5Implementar um programa em Python que solicita ao utilizador dois valores numéricos e no
# caso de serem diferentes indica qual o maior
n1=int(input('introduzir um valor:'))
n2=int(input('introduzir outro valor:'))

if (n1>n2):
    print('valor de ', n1, 'é superior a', n2)
if(n2>n1):
    print('valor de ', n2, 'é superior a', n1)
if(n1==n2):
    print('os valores são iguais')
#6-Implementar um programa em Python que solicita ao utilizador três valores numéricos e calcular a soma e média dos 3 números inteiros
n1=int(input('insira um numero'))
n2=int(input('insira outro numero'))
n3=int(input('insira outro numero'))
print ((n2*n1*n3)/3, 'valor da médid')
#7Codifique um programa em Python que escreve de forma ordenada, 3 números inteiros
# inseridos pelo utilizador.
numero1=int(input('insira um numero'))
numero2=int(input('insira outro numero'))
numero3=int(input('insira outro numero'))

if(numero1<numero2):
    if(numero1<numero3):
        if(numero2<numero3):
            print(numero1, numero2,numero3)
        else:
            print(numero1,numero3,numero2)
if(numero2<numero1):
    if(numero2<numero3):
        if(numero1<numero3):
            print(numero2,numero1,numero3)
        else:
            print(numero2,numero3,numero1)
if(numero3<numero1):
    if(numero3<numero2):
        if(numero1<numero2):
            print(numero3,numero1,numero2)
        else:
            print(numero3,numero2,numero1)

#pode se escrever de outra forma
'''Exercício 8
Desenvolver um programa em Python que solicite ao utilizador um valor inteiro até 10 e como
resultado escreve esse valor por extenso'''
# exer2>0 com -1 significa que nao esta a encontrar na função
valor=int(input('introduza um valor:'))

if(valor>=1 and valor<=10):
    if(valor==1):
        print('um')
    elif(valor==2):
        print('dois')
    elif(valor==3):
        print('dois')
    elif(valor==4):
        print('dois')
    elif(valor==5):
        print('dois')
    elif(valor==6):
        print('dois')
    elif(valor==7):
        print('dois')
    elif(valor==8):
        print('dois')
    else:
        print('10')

#exercicio 9
'''Implementar um programa que mediante a introdução de um valor inteiro, que representa o
número de um mês, indica quantos dias tem esse mês. '''
valor=int(input('introduza um número:'))
calculo=valor%2  
if(valor>=1 and valor<=12):
    if calculo==1:
        print('mês com 31 dias')
    elif calculo==2 :
        print('mês com 28 dias')
    else:
        print('o mês tem 30 dias')