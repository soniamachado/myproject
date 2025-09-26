print('lab14_EXERC1) Efetuar a leitura dos dados do ficheiro sample.txt, através do módulo csv, diretamente para um dicionário:')
import csv #modulo que permite trablhar com ficheiro csv.ficheiros que separa o ficheiro através da ",". 
#CSV comma Separated Values, guarda dados em forma de tabela, onde as colunas são separadas por vírgulas(ou às vezes ; ou \t) e cada linha representa um registo diferente(uma linha da tabela).
'''EXEMPLO DE FICHEIRO CSV
Name,Domain,Country
GOOGLE,google.com,United States
MICROSOFT,microsoft.com,United States
FACEBOOK,facebook.com,United States'''
with open(r'/home/sonia_machado/myproject/python/organizations-100.csv','r')as f:#O with garante que o ficheiro será fechado no fim automaticamente.
    #O r antes do caminho (r'/home/...) significa raw string → evita que o Python interprete \n ou \t como caracteres especiais.
    result=csv.DictReader(f,delimiter=',')
    for r in result:
        print(r['Name'])
        #DictReader lê o ficheiro CSV e transforma cada linha num dicionário Python
    #DictReader lê o ficheiro CSV e transforma cada linha num dicionário Python
    '''A primeira linha do CSV (ID,Name,Country) é usada como chaves do dicionário.

Cada linha seguinte vira um dicionário com essas chaves.

Exemplo:
Linha no CSV → 2,Siemens,Germany
Dicionário → {'ID': '2', 'Name': 'Siemens', 'Country': 'Germany'}

o for faz percorrer cada linha do ficheiro CSV, e cada linha(o r) é um dicionário'''


print('exercicio1.b')
''') No código anterior implementar as seguintes exceções
➢ KeyError(por exemplo que se tenta aceder a uma chave que não existe)
➢ csv.Error(por exemplo, se o conteúdo do ficheiro não seguir o formato esperado)
➢ FileNotFoundError
➢ Exception(exceção geral)'''
import csv #modulo que permite trablhar com ficheiro csv.ficheiros que separa o ficheiro através da ",".
novo_registo={'Name': 'ong123', 'Country': 'Portugal'}
#primeira parte escrever no csv novos registo
try:
    with open(r'/home/sonia_machado/myproject/python/organizations-100.csv','a')as f:
        escreve=csv.writer(f,delimiter=',')#transforma cada em uma linha nova no ficheiro csv
        escreve.writerow(novo_registo.keys())#dict_keys(['Name', 'Country']):escreve os nomes das colunas
        escreve.writerow(novo_registo.values())#dict_values(['ong123', 'Portugal']):escreve os valores de novo registo
except FileNotFoundError:
    print('caminho/ficheiro não existem')
except csv.Error:#e o contéudo do ficheiro não seguir o formato esperado
    print('formatação incorreta')
except KeyError:
    print('Erro na chave do dicionario')#tentar aceder a uma chave que não existe
except Exception as e: #exceção geral
    print('Erro:{e}')

#segunda parte ler no csv é ler os dados e procurar todos os que têm Country=Uzebequistao
try:
    with open(r'/home/sonia_machado/myproject/python/organizations-100.csv','r')as f:
        leitura=csv.DictReader(f)
        for txt in leitura:
            if(txt['Country']=='Uzebequistao'):
                print(txt)
except FileNotFoundError:
    print('caminho/ficheiro não existem')
except csv.Error:
    print('formatação incorreta')
except KeyError:
    print('Erro na chave do dicionario')
except Exception as e:
    print('Erro:{e}')

'''É uma biblioteca do Python para análise e manipulação de dados.
O nome vem de "Panel Data" (dados em painel), mas hoje em dia é quase um sinónimo de "análise de dados em Python".
É das bibliotecas mais usadas em ciência de dados, machine learning, estatística, finanças, cibersegurança (logs), etc.'''
print('lab14_exer2')
#O ficheiro sample.txt também pode ser lido através do módulo pandas:
import pandas as pd#importa a bibliotexa pandas e dá-lhe o apelido pd
#pandas é uma biblioteca poderosa para análise e manipulação de dados em Python, parecido com excel ou sql.
result=pd.read_csv(r'/home/sonia_machado/Python_EISNT/leitura_de_dados/organizations.csv')
#lÊ o ficheiro CSV (read_csv) e guarda o resultado na variável result, DataFrame (tabela), cada linha do csv vira linha no dataframe e cada coluna vira uma coluna no dataframe
print(result.head())
#mostra as 5 primeiras linhas da tabela(padrão do head())

import pandas as pd
result=pd.read_csv(r'/home/sonia_machado/myproject/python/organizations-100.csv')
print(result.head(10))
#Mostra as 10 primeiras linhas.

import pandas as pd
result=pd.read_csv(r'/home/sonia_machado/myproject/python/organizations-100.csv')
print(result.tail(3))
#Mostra as 3 últimas linhas da tabela.

print('lab14_exer3')
''' exer3
1. Entre [] está se a falar de colunas. exemplo df[['DATE,'REGION']].head(5) mostra 5 linhas apenas das colunas DATE e REGION

2.Selcionar linhas por posição.formas de extrair a linha print(df[3:10])exemplo do valor-MOSTRA AS LINHAS DA 3 até à 9
#as primeiras linhas que eu defenir é através do médtod head print(df[['DATE,'REGION']].head(5))
#ver a amostra no final é através do  print(df[['DATE,'REGION']].tail(5)), colunas DATE e REGION

3 Selecionar linhas e colunas pelo indice, método print(df.iloc[linhas , [colunas]]) seleciona linhas e colunas pelo indice(iloc)-trabalha com índices numéricos(posição pura, sem nomes)
#Aqui as colunas são sempre passadas em lista.
df.iloc[0:5, [0, 2]]
Mostra as 5 primeiras linhas e apenas as colunas de índice 0 e 2.

posso tambem procurar a coluna e lista através do método df.loc[ 10:20, ['units', 'salaes]], mais ums
vez quando estou a ver colunas colocar em formarto de listas, Selecionar linhas e colunas pelo nome(loc)-trabalha com nomes de colunas e rótulos de linhas

4.Selecionar linhas e colunas pelo nome (loc)
df_selected=df.loc[10:20, ['units', 'sales']]
print(df_selected.to_string(index=False))
aqui pegaste nas linhas 10 e 20 e só nas colunas units e sales, e imprime a tablea sem mostrar a coluna de índices

5
filtragem a nível de linhas + colunas depois
print(df[df['units]>30]['Region])---> primeir seleciona só as linhas onde units>30, depois, dessas linhas, mostras só a coluna Region
PRIMEIRO AS LINHAS E DEPOIS AS COLUNAS NA FILTRAGEM.

print(df[(df['units']>30) & (df['sales']>500)]['Region'])mostra a coluna Region, mas apenas para linha onde unit>30 e sales>500, se fosse |(pipe) seria ou'''

#MÉTODO QUERY
'''df_query=df.query('Units==35 and Sales>500)
faz o mesmo que o exemplo de cima, mas com uma sintaze parecida com SQL'''