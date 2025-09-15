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
h=0
while h<=100:
    print(h,'x',h,'=',h*h)
    h=h+1

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

print ("exercicio 9")
'''Desenvolver um programa, que solicita ao utilizador dois valores, e escreve no terminal todos
os números primos entre esses dois valores, assim que analisar um número divisível por 5
termina o programa'''
def numero_primo(inteiro):
    if inteiro > 1:
        for i in range(2, inteiro):
            if (inteiro % i) == 0:
                return False
        return True
    else:
        return False        
'''No seu código, quando inteiro = 2, o loop for i in range(2, inteiro): é range(2, 2), que é vazio, logo o corpo do loop não é executado, e a função retorna True diretamente, indicando que 2 é primo'''   
valor1=int(input('indique o primeiro valor'))
valor2=int(input('indique o segundo valor'))

for i in range(valor1, valor2+1):
    if (i%5==0):
        print('termina o programa')
        break
    z=numero_primo(i)
    if(z==True):
        print (i,'é primo')
    else:
        print(i,'não é primo')  
'''Desenvolver um programa, que solicita ao utilizador dois valores, e escreve no terminal todos
os números primos entre esses dois valores, mas não escreve os primos entre 10 e 20.'''
a=int(input('introduza um valor'))
b=int(input('introduza outro valor'))

def primo(n):
    p=True
    for i in range(2,n):
        if (n%i ==0 ):
            p=False
            break

    return p
 
for i in range(a,b+1):
    if(i>=10 and i<=20):
       continue
    c=primo(i)
    if(c==True):
       print("..", i)

'''Quando i está entre 10 e 20 (inclusive), o comando continue faz com que o programa ignore o que vier depois dentro do loop naquela volta específica e vá direto para a próxima iteração, ou seja, não executa o restante do código para esses valores de i'''
print("exer.11- Alterar o programa anterior de forma a analisar os valores do maior para o menor.")
a=int(input('introduza um valor'))
b=int(input('introduza outro valor'))

def primo(n):
 p=True
 for i in range(2,n):
    if (n%i ==0 ):
        p=False
        break

 return p
 
for i in reversed(range(a,b+1)):
    print(i)
    if(i<10 and i>20):
        c=primo(i)
        if(c==True):
            print("..", i)

'''
i=b
while(i>=a):
    if(i<10 or i>20):
        c=primo(i)
        if(c==True):
            print('...', i)
            
    i=i-1'''

print('Desenvolver um programa que imprime no terminal o fatorial dos valores entre 1 e 15')
#fatorial de um número n é o produto de todos os inteiros positivos menores ou iguais a n. É representado por n! e definido como:
#n! = n × (n - 1) × (n - 2) × ... × 2 × 1, com a exceção de 0! que é igual a 1.
#Por exemplo, 5! = 5 × 4 × 3 × 2 × 1 = 120.
for i in range(1,16):
    fatorial=1
    for j in range(1,i+1):
        fatorial=fatorial*j
    print(i,'! =',fatorial) 


def fatorial(numero):
   fat=1
   for k in range(2,numero+1):
     fat=fat*k

   return fat

a=int(input("Introduza um valor:"))
b=int(input("Introduza outro valor:"))

for i in range(a,b+1):
   f=fatorial(i)
   
   print(i,"!=",f) 

   
'''
for i in range(a,b+1):
   fat=1
   for k in range(2,i+1):
     fat=fat*k
   
   print(i,"!=",fat)'''