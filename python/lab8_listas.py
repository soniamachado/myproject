print('exercicio 1')
#Implementar o seguinte código e após a correção do erro da linha 5 e efetuar as seguintes
#alterações:
temperatura=[12,19,21,17,18,14]
temperatura[0]=11
print('Novo valor para a posição de indice0:', temperatura[0])
temperatura[5]=13
temperatura[0]=99
temperatura.append(50)
a=temperatura[1]
b=temperatura[2]
print(a,',',b)
print(temperatura[1], ',',temperatura[2])
temperatura.insert(0,60) #método insert, dicionar o elemento com valor 60 no início da lista
# Escreve no terminal a quantidade de elementos da lista através do método count
print(temperatura.count(12))
print(len(temperatura))
del temperatura[1]

print('/nexercicio3')
#Codificar e verificar os resultados do código abaixo:
def print_array(arr):
    for x in arr:
        print(x)

temperaturas=[10,21,12,22,22]
print('elementos iniciais do array, com dimensões', len(temperaturas))
print_array(temperaturas)#resultado final  10 21 12 22 22 

print('Adicionar um novo elemento no array na posição 5')
temperaturas.insert(5,21)#resultado final  10 21 12 22 22 21 
print_array(temperaturas)

print('adicionar um novo elemento no array na posição 5')
temperaturas.insert(5,21) #resultado final  10 21 12 22 22 21 21 
print_array(temperaturas)

temperaturas.pop(0)#elimina o elemento e guarda
print('eliminar o elemento de index 0')
print_array(temperaturas)#resultado final   21 12 22 22 21 21 

temperaturas.remove(22)
print('eliminar elemento ocurrência do valor 22')
print_array(temperaturas)#resultado final   21 12 22 21 21 


print('/nexercicio4')
#Implementar uma função em Python que recebe uma lista de inteiros e retorna a quantidade
#de números maiores que 10 na lista.

def contar_maiores_que_dez(lista):
    contador = 0
    for num in lista:
        if num > 10:
            contador += 1 #contador = contador + 1
    return contador 

temperaturas=[10,21,12,22,12]
n=contar_maiores_que_dez(temperaturas)
print('quantidade de valores superiores a 10:', n)

def dobro_de_cada_elemento(temperaturas):
   #lista_dobro=[]
   for v in temperaturas:
      print(v*2) #print-só mostra na tela, não o podes usar/guardar
      #melhorar lista_dobro.append(v*2)
    #return lista_dobro 

dobro_de_cada_elemento(temperaturas) #se eu quero que a função devolva então coloco sobre uma variável, n
'''Quando uma função tem return, ela devolve um resultado.
Se tu não o guardares em lado nenhum → o Python calcula, devolve… mas como não foi armazenado, perdes o valor.'''

print('/nexercicio6')
#Desenvolver uma função que recebe uma lista de textos e devolve uma lista com os elementos
#com mais de 10 caracteres. 
textos=['um', 'dois', 'trÊs', 'quatro']

def elementos_de_10(lista):
    textos_finais=[]
    for i in textos:
     if (len(i)> 10):
        textos_finais.append(i)
    return textos_finais

l=elementos_de_10(textos)
print(l)

print('/nexercicio7')
#Implementar uma função que devolve o maior número de uma lista (sem usar a função max)
def max_numero(n):
    a=0
    for i in numeros:
        if a<i:
            a=i;
    return a
numeros=[1,3,4,3,8,9,2,14,33]
print('numero é', max_numero(numeros))

print('/nexercicio8')
'''Implementar uma função que recebe uma lista de inteiros e um inteiro L e devolva uma lista
com os números da lista que são maiores ou iguais que L.'''
def lista_maior_ou_igual_L(n, L):
    nova=[]
    for i in numeros:
      if L<= i:
         nova.append(i)
    return nova

L=5
print('numero é', lista_maior_ou_igual_L(numeros, L))

print('/nexercicio9')
#devolver uma função que recebe uma string e devolva o número de vogais que ela contém
def número_de_vogais(textos):
    nova=[]
    vogais=['a','e','i','o','u']
    for i in textos:
      if i==vogais:
        nova.append(i)

    valor= len(nova)
    return valor
palavra=['adriana']
print('a lista contem as seguintes vogais', número_de_vogais(palavra))
'''professor fez
def voga(text):
    contador=0
    for c in txt:
        if(c=='a' or c=='e' or c=='i' or c==o or c==u')
        contador=contador+1
        return contador
'''
print('/nexercicio10')
def soma_listas(lista_valores):
   soma=0
   for x in lista_valores:
      soma=soma+x
   return soma
temperaturas=[10,21,15]
s=soma_listas(temperaturas)
print('soma de todos os elementosd da lista',s)

#the end keyword: the keyword argument end can be used to avoid the newline after the output, or end the output with a different string: with a different string
phrase=['printed', 'with', 'a', 'dash', 'in', 'between']
for word in phrase:
    print(word, end='-')
# Output: printed-with-a-dash-in-between-