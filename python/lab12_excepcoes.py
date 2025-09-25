#TRY
#exercicio1 - Executar o código abaixo e verificar que após o erro retornado, as instruções seguintes já nãosão executadas.
try:
    print('Início do bloco try')
    valor2=125
    valor3=0
    print('valor 2:', valor2, 'valor3:',valor3)
except NameError:
    print('variável não está definida')

    #exercicio3
    '''No seguimento do exercício anterior, é pretendido dividir a variável valor2 pela variável valor3,
e implementar a exceção zeroDivisionError, para tratar os erros gerados no caso da divisão por
zero'''
try:
    
    valor1=125
    valor2=5
    valor3=valor1/valor2
    print(valor1,'/', valor2, '=',valor3)
    

except ZeroDivisionError:
    print('divisão por erro')
except NameError:
    print('Varíavel não definida')
finally:#código é sempre executada, caso acha erro ou não
    print('cálculos concluído')

#xercicio4
'''O bloco de código finally é executado quer tenham sido gerado erros ou não, assim
prentende-se implementar esta funcionalidade no exercício anterior:'''
def divisao(a,b):
    try:
    
   
        valor3=a/b
        print(a,'/', b, '=',valor3)
    

    except ZeroDivisionError:
        print('tentativa de devisão por 0.')
    except NameError:
        print('Varíavel não definida')
    finally:#código é sempre executada, caso acha erro ou não
        print('cálculos concluído')

print('inicio...')
n=divisao(2,0)
print('continuacao..')
print('fim.')

#exercicio7- A implementação de exceções também pode ser utilizada para validações. 
try:
    numero=int(input('introduza um valor'))
    if numero>100:
        raise ValueError('Erro na validação')
    if(numero<100):
        raise ValueError('Erro na validação')
    if(numero==100):
        raise ValueError('Erro na validação')
        
    print('fim do try')
except ValueError as e:
    print('An error occurred:', str(e))
#O RAISE assim que é ativado segue para o except


#exercicio10-No código abaixo são apresentadas algumas instruções para gerir uma lista de dicionários:


'''
for emp in employees:
    print(emp['Name'])
    print(emp['age'])
    emp['age']=18'''
#listar todos os elementos para função
def listar_empregados(lista_empregados):
     for emp in employees:
        print('Name:', emp['Name'], 'salary:', emp['Salary'], 'age:', emp['age'])

def inserir_empregados(lista_empregados):
    try:#se houvesse erro programa terminava abruptamente
        nome=input('nome')
        salario=int(input('salario:'))
        idade=int(input('idade:'))
#adicionar funcionario temperadamente
        novo_empregado={'Name': nome, 'Salary': salario, 'age': idade}
        lista_empregados.append(novo_empregado)
        return lista_empregados
    except Exception as e:#“apanha” qualquer erro que aconteça no bloco try. Exception é a classe “mãe” de quase todos os erros em Python (ValueError, TypeError, KeyError
        #'as e' guarda o erro dentro da variável e.
        print('erro na inserção de empregados:', str(e))# vai me indicar que tipo de erro consiste 
        return lista_empregados
        #evita que o programa pare de repente
        #dá feedback ao utilizador sobre o que aconteceu de errado
        #É muito útil quando estamos a pedir inputs ao utilizador, que podem ser errados
def eliminar_empregado(lista_empregados):
    try: 
        nome=input('nome do empregado a eliminar:')
        eliminado=False
        for emp in lista_empregados:
            if emp['Name']==nome:
                lista_empregados.remove(emp)
                eliminado =True#se ficar com valor true significa que eliminei um elemento
        if eliminado==True:
            print('Empregado removido com sucesso')
        else:
            print('empregado não encontrado')
        return lista_empregados
    except Exception as e:
        print('erro na inserção de empregados:', str(e))# vai me indicar que tipo de erro consiste 
        return lista_empregados

def atualizar_empregado(employees):
    try: 
        nome=input('nome do empregado atualizar:')
        novo_salario=int(input('salario:'))
        nova_idade=int(input('idade:'))
        atualizado=False
        for emp in employees:
            if emp['Name']==nome:
                emp['Salary']=novo_salario
                emp['age']=nova_idade
                atualizado==True
        if atualizado==True:
            print('Empregado atualizado com sucesso')
        else:
            print('Empregado não encontrado para atualização')
        return employees
    except Exception as e:
        print('erro na inserção de empregados:', str(e))# vai me indicar que tipo de erro consiste 
        return employees  
def pesquisar_empregado(employees):
    try: 
        nome=input ('Nome do empregado a eliminar') 
        pesquisa=False
        for emp in employees:
            if emp['Name']==nome:
                print('Empregado encontrado:')
                print('Name:', emp['Name'], 'salary:', emp['Salary'], 'age:', emp['age'])
                pesquisa =True#se ficar com valor true significa que eliminei um elemento
        if pesquisa==False:
            print('Empregado não encontrado')
        
    except Exception as e:
        print('erro na inserção de empregados:', str(e))# vai me indicar que tipo de erro consiste 
        return employees



employees=[
    {'Name':'Sravan','Salary':1000, 'age':21},
    {'Name':'Raghu','Salary':1100, 'age':19}]

opcao=1
while True:
    print('1-Inserir empregado')
    print('2- Eliminar empregado')
    print('3-Atualixar empregado')
    print('4 Pesquisar empregado por nome')
    print('5- Listar empregados')
    print('6- Sair')
    opcao=int(input('Opção:'))

    if(opcao==1):
        print('Inserir empregado')
        employees=inserir_empregados(employees)
        
    elif(opcao==2):
        print('..eliminar')
        employees=eliminar_empregado(employees)
    elif(opcao==3):
        print('..atualizar')
        employees=atualizar_empregado(employees)
    elif(opcao==4):
        print('..pesquisar')

    elif(opcao==5):
        print('..listar')
        pesquisar_empregado(employees)
    
    elif(opcao==6):
        print('..sair')
        break