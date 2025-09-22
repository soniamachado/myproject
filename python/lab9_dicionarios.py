a={'apple':'fruit', 'beetroot':'vegetable','cake':'desert'}
a['doughnut']='snack' #adicionar o par com a chave doughnut e valor snack
print(a['apple']) #escrever no terminal o valor da chave apple

#adicionar o par com a chave water e valor drink
a['water']='drink'
#escrever no terminal o valor da chave cake
print(a['cake'])
#alterar o valor da chave para sweet
a['cake']='sweet'
# Escrever todo o conteúdo do dicionário “a” através da instrução: print(a)
print(a)

print('/nexericio9.2 - ciclo for')
d1={'one':11,'two':22,'three':33,'four':44,'five':55}
print('ciclo FOR')
for k in d1:
    print('Key:',k,'Value:',d1[k])
#exemplo vai passar pot todas as chaves do dicionário(one, two, three, four, five) e passar respectivo valor, é x e f(x)
print('\nPrint')
print(d1)

my_dict={'apple':1, 'banana':2, 'orange':3}
for value in my_dict.values():
    print(value)
'''my_dict.keys() → devolve as chaves (apple, banana, orange)

my_dict.values() → devolve os valores (1, 2, 3)

my_dict.items() → devolve pares (chave, valor) (('apple', 1) etc.)'''

print('/nexericio9.3')
#exercicio9.3
#Considerando o código abaixo determine as chaves e valores idênticos nos dicionários a e b.
a={'joe':85, 'peter':87, 'jack':91}
b={'joe':90, 'peter':85, 'jack':88}

for c,v in a.items():
    for c2,v2 in b.items():
        if(v==v2 and c==c2):
            print('chave:',c,'valor identidico:',v)

'''ou
outra sujestão
for chave, valor in a.items():
    if chave in b and b[chave] == valor:
        print('chave:', chave, 'valor idêntico:', valor)

ou
for c1 in a:
    print('chave:', c1, 'valor:', a[c1])
        for c2 in b:
            print('chave:', c2, 'valor:', a[c2])
                #comparo primeiro os valores e depois a chave
                if(a[c1]==b[c2] and c1==c2):
                    print('chave identica:', c1, 'valor identico:', a[c1])'''

print('/nexericio9.4')
#Desenvolver o código que permite remover os valores pares do seguinte dicionário:
#Para eliminar um elemento de um dicionário pode ser utilizado o método del(key)
dic={'1':10, '2':20, '3':30, '4':40,'5':51,'6':63}
#para eliminar só os pares
dic_pares={}
for chave,valor in dic.items():
#for chave in dic:
    if valor%2==0:
        dic_pares[chave]=valor

for chave1 in dic_pares:
    del dic[chave1]


print(dic)  

print('exercicio_9.5')
#Desenvolver uma função, que recebe um dicionário e retorna um outro dicionário mas semvalores repetidos.
def obtem_valores_distintos(disc1):
    dic_aux={}
    for c3,v3 in disc1.items():
    #verificar os numeros repetidos e colocar um novo dicionario sem os numeros repetidos
       if v3 not in dic_aux.values():
        dic_aux[c3]=v3

    return dic_aux

input={'1':10, '2':20, '3':30, '4':30,'5':51,'6':60}

dic2=obtem_valores_distintos(input)
print(dic2)

print('/nexercicio_9.6')
#exercicio9.6---fazer com chat gpt
'''Desenvolver uma função, que recebe dois dicionário e junta-os, retornando um dicionário
único(mesmo com valores repetidos)'''
def unir_dicionarios(x,z):
    dic3={}
    for chave3,valor3 in dictionary1.items():
        dic3[chave]=valor
    
    for chave4,valor4 in dictionary2.items():
        dic3[chave]=valor
    return dic3

dictionary1 = {'chave1': 10, 'chave2': 20}
dictionary2 = {'chave2': 30, 'chave3': 40}

resultado=unir_dicionarios(dictionary1,dictionary1)


print('exercicio_9.7.a')
#exercicio9.7 a.
'''for chave5, nota in scores.items():
    for i in nota:
        print('indice', i)'''
# implementar as seguintes funções:Media_Estudante(notas):Esta função retorna uma lista com a média de cada estudante

def calcula_media(alunos):
    dic_media= {}

    for nome, nota in alunos.items(): #nome-recebe chave animais e nota -recebe lista associado aos animais
        soma=0
        contador=0
        for i in nota:#percore cada número da lista
            soma=soma+i
            contador=contador+1
        media=soma/contador
        dic_media[nome]=media #chave=nome, valor=media

    return dic_media;


scores= {
    'animal':[10,30,40,50],
     'bimal':[85,74,69,47],
        'Tarun':[65,35,87,14],
        'Akash':[74,12,36,75]
        }

dic_aux=calcula_media(scores)

for nome,media in dic_aux.items():
    print(nome, '=', media)

#exercicio9.7 b. ) Media_Global(notas)

print('\nexercicio_9.7.b')
def calcula_media_global(alunos):
    
    soma=0
    contador=0
    for nome, nota in alunos.items():
        for i in nota:
            soma=soma+i
            contador=contador+1
        media=soma/contador
        

    return media;

dic_aux={}
dic_aux=calcula_media_global(scores)

for nome,media in dic_aux.items():
    print(nome, '=', media)

m=calcula_media_global(scores)
print('media global:', m)

media_total=0
contatdor_total=0
soma_total=0
for nome, media in dic_aux.items():
    soma_total= soma_total+media
    contador_total=contador_total+1

media_total=soma_total/soma_total
print('media total:', media_total)

#exercicio9.7 c. Aluno_nota_mais_alta(notas)
print('exercicio_9.7.c')
def aluno_nota_mais_alta(alunos):
    nota_mais_alta=0   
    for nome, nota in alunos.items():
        for i in nota:
           
            if nota_mais_alta <i:
                nota_mais_alta=i
                nome_aluno=nome#corresponde ao nome do aluno com nota mais alta

            
        

    return nota_mais_alta, nome_aluno;

scores= {
    'animal':[10,30,40,50],
     'bimal':[85,74,69,47],
        'Tarun':[65,35,87,14],
        'Akash':[74,12,36,75]
        }
dic_aux={}

#com duas variáveis
nome_aluno,nota_mais_alta=aluno_nota_mais_alta(scores)
print('aluni com melhor nota', nome_aluno, 'com a nota' , nota_mais_alta)


print('exercicio_9.8')
#exercicio9.8 Desenvolver o código necessário para que gerir o dicionário grades
def ListarDisciplinas(disciplinas):
    if not disciplinas:
        print('nenhuma disciplina inserida')
        return  
    print('\n Disciplinas:')
    for chave, valor in disciplinas.items(): 
        print('disciplina:',chave)
        print('...nota',valor)
        #print(f"-{chave}: {valor}")

def InserirDisciplinas(disciplinas):
    print('inserir nota..')
    nova_disciplina=input('introduzur disciplina:').strip()#remove espaços em branco no inicio e no fim
    nova_nota=float(input('introduzir nota:'))
    #verifica se está a disciplina no dicionario
    verificar_se_existe=disciplinas.get(nova_disciplina) #Tenta buscar o valor associado a uma chave no dicionário.Se a chave não existe, devolve None
    #nova_disciplina → o nome da disciplina que o utilizador escreveu.
    #disciplinas.get(nova_disciplina) → vai procurar essa disciplina no dicionário
    #Se existir, devolve a nota já guardada.
    #Se não existir, devolve None
    if(verificar_se_existe is None):
        disciplinas[nova_disciplina]=nova_nota              
    else:
        print('disciplina já existente')

def AtualizarDisciplinas(disciplinas):
    print('atualizar disciplina')
    print('inserir nota..')
    disciplina_atual=input('introduzur disciplina:')
    nova_nota=float(input('introduzir nota:'))
    #verifica se está a disciplina no dicionario
    verificar_se_existe=disciplinas.get(disciplina_atual)
    

    if(verificar_se_existe is None):
            disciplinas[disciplina_atual]=nova_nota              
    else:
            print('disciplina inexistente')



disciplinas={}
while True:
    print('1-inserir nota')
    print('2-atualizar disciplina')
    print('3-procurar disciplinca')
    print('4 eliminar disciplina')
    print('5-Listar')
    print('6-Sair')
    opcao=int(input('opção;'))

    if(opcao==1):
        
        InserirDisciplinas(disciplinas)

    elif(opcao==2):
        print('atualizar disciplina')
        print('inserir nota..')
        disciplina_atual=input('introduzur disciplina:')
        nova_nota=float(input('introduzir nota:'))
    #verifica se está a disciplina no dicionario
        verificar_se_existe=disciplinas.get(disciplina_atual)
    

        if(verificar_se_existe is None):
            disciplinas[disciplina_atual]=nova_nota              
        else:
            print('disciplina inexistente')


    elif(opcao==3):
        print('procurar disciplina') 
        disciplina_procurar=input('disciplina a procurar:')
        flag=False
        for chave, valor in disciplinas.items():
            if(chave==disciplina_procurar):
                print('nota',valor)
                flag=True
                
            if(flag==False):
                print('disciplina inexistente')

    elif(opcao==4):
        print('eliminar disciplina') 
        disciplina_eliminar=input('introduzir disciplina:')
        if (disciplina_eliminar in 'introduzir disciplina'):
            del disciplina_eliminar[disciplina_eliminar] 
            print('eliminação efetuada com sucesso')
    elif(opcao==5):
        ListarDisciplinas(disciplinas)
        
    else:
        break;

print('exercicio_9.9')
#exercicio9.9 Através do exemplo de dicionários aninhados:
students={'alice':{'age':20, 'grade':'A'},
           'BOB':{'age':22, 'grade':'B'          
          }}
#inserir novo valor
students['viktor']={'age':20, 'grade':'c'}

#remover a alice
'''del students['alice']'''

#calcular o aluno mais velho
for student,details in students.items():
    print('Nome:', student)
    print('Age:', details['age'])
    print('Grade:', details['grade'])

#verificar se existe aluno com 18 anos
lista_de_maiores_de_18=[]
for student,details in students.items():
    if details['age']==18:
        lista_de_maiores_de_18.append()
    print(len(lista_de_maiores_de_18))

'''professor
existe=False
for x,y in student.item():
    if(y['age']==18):
    #print('aluno',x,'tem 18 anos)
    existe=True
    
if(existe==True):
    print('existe alunos com 18 anos')
'''