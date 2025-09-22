#exercicio1
my_tuple=(10,'hello', 3.14)
print('[0]:', my_tuple[0])
print('[1]:', my_tuple[1])
print('[2]:', my_tuple[2])

print('FOR:')
for idx,valor in enumerate(my_tuple):#idx é o indice, valor é o elemento
    print('indice=', idx, valor)

'''TUPLAS ANINHADAS- TUPLAS DENTRO DE TUPLAS: usar Quando queres guardar dados que não devem ser alterados.
Podem ser usadas como chaves de dicionário (listas não podem, porque são mutáveis)
Exemplos:
t = (1, (2, 3), (4, 5))
print(t[1][0])  # 2'''
#b) defina um novo tuplo com os 
# elementos: 20, “ALL” e 0.56, e escrever os seus 
#elementos no terminal  
my_tuple_2=(20,'ALL',0.56)
print('FOR(my_tuple_2):')
for idx2,valor2 in enumerate(my_tuple_2):
    print('indice=',idx2, valor2)

#outra forma de escrever
print('FOR elemebti(my_tuple_2):')
for elemento in my_tuple_2:
    print(elemento)

#alinea c efinir um terceiro tuplo como resultado da junção dos dois tuplos anteriores, e 
#escrever os elementos deste novo tuplo no terminal 
my_tuple_3=my_tuple + my_tuple_2
for elemento in my_tuple_3:
    print(elemento)

if((20 in my_tuple_3)==True):
    print('elemento 3 existe no tuplo')
else:
    print('elemento3 não existe no tuplo')

#d-desenpacutamento dos valores do tuplo
a,b,c=my_tuple
print('a=',a)
print('b=,',b)
print('c=',c)

#
lista_valores=list(my_tuple_3)
print('nova lista:')
print(lista_valores)

lista_valores=list(my_tuple_3)
print('nova lista:')
print(lista_valores)
lista_valores.append(20)
print(lista_valores)

#está realizado um novo tuplo
print('Novo tuplo my_tiple_4:')
my_tuple4=tuple(lista_valores)
print(my_tuple4)

#para realizar a quantidade no tuplo é a mesma com um len
print('tamanho do my_tuple_4:', len(my_tuple4))

#exercicio 10.2
words=('welcome', 'to', 'our','class', 'a', 'nice', 'place')
#a
n=words.count('to')
print('quantidade de ocurrencias de to', n)

#b)
n=words.index('nice')
print("posição de 'nice'", n)

#c
#novo_tuplo=()
novo_lista=[]
for elemento in words:
    novo_lista.append(elemento.upper())

novo_tuplo=tuple(novo_lista)
print(novo_tuplo)

#d - Transformar o tuplo numa única string
texto=''.join(words)
print('Text:', texto)

str_texto=''
for elemento in words:
    str_texto=str_texto + elemento

print('str_texto:', str_texto)
#-Determinar a quantidade de elementos do tupl
print("tamanho de 'words':", len(words))
#f-Determinar a quantidade de elementos do tuplo 
words2=words+('to', 'work')
print('words2:', words2)

my_dict={}
for i in range(0,len(words)):
    my_dict[i]=words[i]

my_dict[len(words)+1]='to'
my_dict[len(words)+2]='work'

print(my_dict)

#g
def procura_ocurrencias(tuplo, string):
    n=tuplo.count(string)
    return n

#quando invocar a função já deve estar predefinida
n=procura_ocurrencias(words, 'to')
print("g) Ocurrencias de 'to':", n)


#3.c settingd
habilidades_pessoais={'Python','Javascript','SQL', 'Machine learning'}
habilidades_procuradas={'Python','AI', 'Data Science'}
print('habildades_pessoais')
for elemento in habilidades_pessoais:
    print(elemento)

print('habildades_procuradas')
for elemento in habilidades_procuradas:
    print(elemento)

print('Elementos em comun:')
habilidades_comuns=habilidades_pessoais & habilidades_procuradas
print(habilidades_comuns)

#3-d Definir um novo set com resultado da junção entre os dois sets acima 
#descritos(através do método union ou operadoor “|”) 

print('junção dos dois conjuntos:')
habilidades=habilidades_pessoais| habilidades_procuradas
print(habilidades)

print('habilidades_procuradas com PHP:')
habilidades_procuradas.add('PHP')
print(habilidades_procuradas)

#e - Verificar as competências do conjunto competencias_desejadas e que não estão 
#presentes no conjunto competencias_pessoa(através método difference ou 
#operador “–“) 
print("habilidades_procuradas e que não estão em habilidades_pessoais")
set_3=habilidades_procuradas - habilidades_pessoais
set_4=habilidades_procuradas.difference(habilidades_pessoais)

'''f-Verficar se os conjuntos têm algum elemento em comun, através do método 
isdisjoint(): 
Set1.isdisjoint(Set1) – retorna True caso não existe nenhum elemento em comum '''
#verificar se existe algum elemento em comun
if(habilidades_procuradas.isdisjoint(habilidades_pessoais)==False):
    print('existem elementos em comum')
else:
    print('não existem elementos em comum')