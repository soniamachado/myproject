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
