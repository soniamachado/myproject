#executar o seguinte código pyhton
x=10
y=15
z=x+y
print("soma de x com y=',z")
print("tipo de dados da variável z:", type (z))

""" Exercício 3
Implementar um programa em Python com os seguintes requisitos:
o atribuir o valor 100.78 para a variável total
o calcular para uma outra variável o dobro do valor da variável total
o calcular para uma outra variável o triplo do valor da variável total
De salientar que todos os valores calculados anteriormente devem ser escritos no terminal"""
var1=100.79
var2=2*var1
var3=3*var1

print ('var1=', var1,'var2=',var2,'var3=',var3)

#exercicio 4
x=15.56
y=30.15
z=45.3
(x2,y2,z2)=(x,y,z)
print('X=',x2)
print('Y=',y2)
print("Z=",z2)

s1="Welcome to"
s1="Pyhton"

#exercicio5
s1='Welcome to '
s2='python'

s3=s1+s2

print(s3)

x,y,z='Orange','Banana','Cherry'
print(x)
print(y)
print(z)

x=y=z='Orange'
print(x)
print(y)
print(z)

x=34.67
x1=int(x)

y=313.99
y1=int(y)

print('a parte inteira de ',x ,' é ',x1)
print('a oarte inteira de ', y,' é ',y1)

print('\nexercicio 9')
str_url='http://pythonworld.com7course'
s2=str_url.replace('.com','.net')
print("str_url",str_url)
print('s2',s2)

count=str_url.count('/')
print('Contagem de "/":',count)
#a primeiro posição é a indice "0"
pos=str_url.find('python')
print('Posição de \"python\":',pos)

#exercicio 2.10
frase= 'o mundo da programação Python'
print(len(frase))
#print(f'o tamanho da string é:{print(len(frase))} caracteres.') ou tamanho =print(len(frase))  print(f'o tamanho da string é:{tamanho}caracteres.')
frase2=frase.upper()
print(frase2)
frase3= frase.replace('o', '*')
print(frase3)

frase4=frase.replace(' ', '\n')
print(frase4)
print(' " ', frase, '"')

#the slice() function The slice() function is used to retunr a specific part of the string, list, dictionary, etc
a=("a","b","c","d","e","f","g","h","i","j")
b=slice(2,5)
print(a[b])
#output:('c','d','e')
