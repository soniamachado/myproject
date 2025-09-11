'''a) Alterar o valor no índice 1 para 12
b) Adicionar o elemento com valor 50 à lista(ao fim da lista, através do
método append)
c) Escrever no terminal o elemento de índice 2 e 3
d) Através do método insert, adicionar o elemento com valor 60 no início da
lista
e) Escreve no terminal a quantidade de elementos da lista através do função
len(<lista>)
f) Eliminar o elemento de índice (através dos métodos del ou pop)
g) Através do método remove, eliminar a primeira ocurrência do valor 12'''
def welcome():
    print('****')
    print('**ola***')
    print('***')

welcome()
#em cima eu invoco a funçao

def double_number(x):
    d=2*x
    return d

valor=int(input('indique um valor'))
a=double_number(valor)
print('dobro de',valor, '=',a);

#exer2
def maior(a,b):
    if a<b:
        print('o valor',a, 'é menor ', b)
    else:
        print('o valor',a, 'é maior ', b)

valor1=int(input('indique um valor1'))
valor2=int(input('indique um valor2'))
maior(valor1,valor2)

#5.4
def soma(a,b,c):
    s=a*b*c
    return s
valor1=int(input('indique um valor1'))
valor2=int(input('indique um valor2'))
valor3=int(input('indique um valor2'))
d=soma(valor1,valor2, valor3)
print('a soma dos 3 valores é', d)
#5.5
def sub(a,b):
    if b==0:
        print('impossivel de realizar a operaçao')
    else:
        k=a/b
        return k;
valor1=int(input('indique um valor1'))
valor2=int(input('indique um valor2'))    
a=sub(valor1,valor2)
print(a)

#5.6
nome=input('indique o seu email')
def validacao(email):
    if '@' not in email:
        print('falta simbolo @')
    else:
        print('email corret')
validacao(nome)
'''ou 
if(len(email)>5):
    if(email.find('@')>0)
        print('email válido')
        
        ou

        if(len(email)>5 and email.find('@'))'''
#if → cada condição é avaliada de forma independente.

#elif → é avaliado só se o if (ou outro elif anterior) for falso
#5.7
'''Implementar uma função que recebe um valor inteiro e escreve no ecrã se o valor é par ou
ímpar'''
def calculte_parity(inteiro):
        a=inteiro%2
        if a==0:
            print('número par')
        else:
            print('numero impar')
    

numero=int(input('indique o numero'))
calculte_parity(numero)
#5.8
'''Implementar uma função, que recebe um valor que representa um ano, e retorna o valor true
no caso do ano ser bissexto, caso contrário retorna false.
➢ Anos bissextos são aqueles que são múltiplos de 4, como 1996, 2000, 2004(que
podem são divisíveis por 4)
➢ Porém, há uma excepção: múltiplos de 100 que não sejam múltiplos de 400
'''
def anos_bissextos(inteiro):
        
        if (inteiro % 4 == 0) or (inteiro % 100 == 0 and inteiro % 400 != 0):
            return True
            #print('True')
        else:
            return False
            #print('false')
numero=int(input('indique um ano'))
z=anos_bissextos(numero)
if(z==True):
     print ('bissexto')
else:
     print('não é bissexto')

#print('O ano que indicou será bisexto', anos_bissextos(numero))
def soma(x,y,z=0):
    s=x+z+z
    return s;
#5.9
a=soma(12,3,1)
print('soma', a)
#5.10
a=soma(12,3) #eu só tenho 2 variáveis, e por isso coloquei em cima z= 0 porque defini como default caso não me indicassem o numero 
print('soma=',a)
def aritmetica(x=0,y=0): #variável com default de 0
    s=x+y
    d=x-y
    return (s,d)
(a,b)=aritmetica(12,3)
print('Soma=',a)#vai retornar o valor da soma
print('subtração=',b)#vai retornar o valor da subtração