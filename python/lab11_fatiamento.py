#exercicio1 Para a variável text apresentada abaixo, indicar o output das seguintes instruções
text='python is powerfull programming language'
print(text[-1])
print(text[-2])
print(text[0])
print(text[7:9])
print(text[-8:])
print(text[:7])
print(text[9:])
print(text[0:10:2])
print(text[-1::1])
print(text[-1:: -1])#vou andae da direita para esquerda


#exercicio2
dias_semana=['segunda','terça','quarta', 'quinta', 'sexta', 'sabado','domingo']
#a
print(dias_semana[4:])
print(dias_semana[0:7:2])
print(dias_semana[1:6:2])
print(dias_semana[0::3])

#exercicio3
letras=['a','b','c','d','e']
'''letras[1:4]=[1,2,3]
print(letras)#substiyuição do b, c ,e
letras[1:2]=[1,2,3] #vai escolher só o b, e acrescentar no elemento b, os 4 números.
print(letras)
letras[:0]=[1,2,3]#forma de introduzir no ínicio
print(letras)'''
#letras[1:5]=[]# forma de remoção apenas apresenta um resultado
#print(letras)

#del letras[1:5]
#print(letras)
#letras[3:100]
#print(letras)
letras_2=letras[:]#copia tudo
print(letras_2)
letras[5:3]
print(letras)
