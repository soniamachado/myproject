#exercico3
nome_ficheiro1='/home/sonia_machado/myproject/python/samples1.txt'

f=open(nome_ficheiro1,'r')
#abrir ficheiro em modo de leitura com r de read; f é o objeto que permite ler as linha a linha
#f=open(nome_ficheiro1,'a')#abrir em modo de acrescentar
#f=open(nome_ficheiro1,'w')#abrir em modo de escrita, apaga o conteudo anterior
#f=open(nome_ficheiro1,'x')#criar um ficheiro novo, se já existir dá erro
while True:
    linha=f.readline()#lê uma linha do ficheiro
    linha=linha.strip()#para eliminar o \n . Extrair os campos de uma linha

    if not linha:#se a linha for vazia not linha, significa que chegaste ao fim do ficheiro
        break

    #alinha a
    #em cima a função percebe quando termina os dados em sequencia em linha
    if(linha.strip().startswith('A')==True):#quando encontrar a linha que inicie com A, e se verificar imprime
        print(linha.strip())#função strip é para retirar os espaços

f.close()#serve para fechares os ficheiros depois de usares, quando está aberto, opython bloqueia o ficheiro e assim fecha esse bloqueio com of.close()
#evista problemas de memória e garantir que outros programas conseguem aceder ao ficheiros sem bloqueio

while True:
    linha=f.readline()
    linha=linha.strip()#para eliminar o \n . Extrair os campos de uma linha

    if not linha:
        break
    
    lista_campos=linha.split(';')#partir /fragmentar o tezxto a partir da stri que determinamos e CRIAMOS A LISTA, EM QUE ; VAI DEFINIR ELEMNTO 0 ANTES DO ; E ELEMENTO 1 DEPOIS ; 
    #split cria uma lista, até o que está escrito até; vai ser um valor, até achar o outro valor vai ser o elemento1
    if(lista_campos[0]=='Afghanistan'):
        print('Pia:',lista_campos[0])
        print('Indicativo:', lista_campos[1])

f.close()
paises=[]
while True:
    linha=f.readline()#cada linha é uma lista com este método
    linha=linha.strip()#para eliminar o \n . Extrair os campos de uma linha

    if not linha:
        break
    
    lista_campos=linha.split(';')#partir /fragmentar o tezxto a partir da stri que determinamos
    #split cria uma lista, até o que está escrito até; vai ser um valor, até achar o outro valor vai ser o elemento1
    
    paises.append(lista_campos[0])
    if(lista_campos[0]=='Afghanistan'):
        print('Pia:',lista_campos[0])
        print('Indicativo:', lista_campos[1])

print('paises ordenados alfabeticamente:')
paises.sort()
print(paises)

f.close()
#melhorias com o código em cima
paises = []

with open('/home/sonia_machado/myproject/python/samples1.txt', 'r') as f:
    for linha in f:
        linha = linha.strip()  # remover espaços e \n no fim
        if not linha:
            continue  # salta linhas vazias

        lista_campos = linha.split(';')  # dividir pelos ";"
        paises.append(lista_campos[0])  # guardar o nome do país

        if lista_campos[0] == 'Afghanistan':
            print('País:', lista_campos[0])
            print('Indicativo:', lista_campos[1])

# ordenar lista de países
print('Países ordenados alfabeticamente:')
paises.sort()
print(paises)
