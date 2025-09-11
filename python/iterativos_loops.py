for i in range(1,15):
    print('loops loops loops loops loops loops', end=' ') #imprime 14 vezes e o end no final é para dar espaço, podia ser com-, '-' , seria loops-loops..
#exercicio 2    Desenvolver um programa, que escreve no terminal os números inteiros de 0 a 100
#exercicio2
'''for i in range (1, 50):
    print(i)'''

#exercicio3 Desenvolver um programa, para escrever os números inteiros de -100 a 100 pela ordem descrita abaixo
'''for i in range (-100, 101):
    print(i)'''

#exercicio4
#implementar um programa, que solicita um valor ao utilizador e escreve a soma dos número inteiro até esse Valor
a=(int(input('dê me um valor:')))
soma=0
for i in range(1,a+1):
    #print(i)
    soma=soma+i

print('soma=',soma)
#fazer uma função com o for em cima
'''def soma(n):
        soma=0
        for i in range(1,n+1):
            print(i)
            soma=soma+1
        return soma

    numero=int(input('valor final:'))
    s=soma(numero)
    print('soma=',s)
'''
#Implementar um programa em Python, que escreve no terminal os números pares de 0 a 100
#exercicio 6.5
numero=int(input('introduza um valor'))
for i in range(1,numero +1):
    if i%2==0:
        print(i, '->par')
    else:
        print(i,'->impar')

#ou
'''
print ('inicio while ...')
i=1
while (i<=100):
    if (i%2==0):
        print(i,"->par")
    else:
        print(i,"->impar")
        
    i=i+1'''
#ou 
#exercicio 6
'''Completar o Código abaixo, para que seja solicitado ao utilizador um número, e enquanto esse valor estiver
for ado intervalo [100,500], continua a solicitar novo número.'''
''' numero=int(input('valor:'))

while(numero<100 or numero >500):
    print("valor incorreto!")
    numero=int(input("introduza de novo um valor correto"))
    
print("Parabens, introduza um valor correto")'''
#É uma estrutura de repetição (loop) que executa um bloco de código enquanto uma condição for verdadeira.
#Se for True, executa o bloco.
#Quando a condição for False, o loop para.
'''contador = 1

while contador <= 5:
    print("Número:", contador)
    contador += 1   # soma +1 a cada volta
'''

#Exercício 7 Codifique um programa em Python que imprime o seguinte padrão: 0x1= 1x1=1 2x2=4 3x3=9 4x4=16 5x5=25 ..
while i<=100:
    print(i,'x',i,'=',i*i)
    i=i+1

'''num=int(input('introduza um valor'))
i=0
while(i<(num+1)):
    print(i,"x", i, '=', i*i)'''

#exercicio 8 
#Implementar uma função que recebe um valor e determina se é primo(em caso afirmativo retorna true).
#um número natural primo, é aquele que possui somente dois divisores distintos: o número 1 e ele próprio.
def numero_primo(inteiro):
    if inteiro > 1:
        for i in range(2, inteiro):
            if (inteiro % i) == 0:
                return False
        return True
    else:
        return False
numero=int(input('indique um numero'))
z=numero_primo(numero)
if(z==True):
        print ('primo')
else:
        print('não é primo')
#print('O número que indicou será primo', numero_primo(numero))
