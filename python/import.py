#Em qualquer programa sempre que é necessário limpar o terminal, é possível através do método system:
import os
os.system('clear')

#Implementar um programa que imprime 10 valores aleatórios entre 100 e 1000, e para cada
#um desses valores verifica se é primo.
import random
n1=random.randint(100,1000)
print(n1)

from datetime import date
today=date.today()


#dd/mm/YY
d1=today.strftime('%d /%m /%Y')
print('d1=', d1)

#textual month, day and year  str string
d2=today.strftime('%B -%d -%Y')
print('d2=',  d2)

#mm/mm/dd/y
d3=today.strftime('%m -%d %y')
print('d3=', d3)

#Month abbrevation, day and year
d4=today.strftime('%b -%d -%Y')
print('d4=', d4)

#exercicio 4
#Desenvolver um novo programa que determina a área e o perímetro de uma circunferência
#através da utilização da constante PI. Area=π*r² e Perímetro=2*π*r 
import math 
raio=int(input('introduz o raio d circunferencia:'))
perimetro=2*math.pi*raio
area=math.pi*raio*raio

print('perimetro da circunfer', perimetro)
print('area da circunfer', area)

#exercicio 5
print('\nexercicio 5')
#Implementar um programa que solicita ao utilizador o seu nome e idade, e escreve no
'''O código abaixo permite a cópia de um ficheiro de uma localização para outra, neste exercício
o utilizador deve indicar o nome de um ficheiro e a sua localização para além da pasta para
onde deve ser copiado.'''
import shutil

src_path=r"/home/sonia_machado/Python_EISNT/exercicio7.5.py"
dsr_path=r"/home/sonia_machado/exer7.5/exercicio7.5.py"

shutil.copy(src_path,dsr_path)
print('copied')
#No Windows, o separador de pastas é \ (barra invertida)

print('\nexercicio 6')  
'''Após a leitura da path de um diretório indicado pelo utilizador imprimir o nome de todos os
ficheiros dessa localização'''
import os
#get all files inside a specific folder
dir_path=r'/home/sonia_machado'
#r antes das aspas significa que a string é uma raw string (string crua).como em pyhtin possui caracteres especiais, como a barra invertida (\), que é usada para escapar outros caracteres. Ao usar o prefixo r, você indica que a string deve ser tratada literalmente, ou seja, sem interpretar esses caracteres especiais.
#O Python não interpreta os escapes, lê a string tal como está escrita:
#dir_path = '/home/sonia_machado'
#dir_path = r'/home/sonia_machado'

#verificar todos 
for f in os.scandir(dir_path):
    if (f.is_dir()==True):
        print(f.name)

'''os.scandir(dir_path) devolve um iterador com todos os entradas dessa pasta (ficheiros e diretórios).
Cada f não é só uma string, é um objeto DirEntry que traz várias informações (nome, se é diretório, se é ficheiro, etc.).'''

'''Para cada entrada, verificas se é uma pasta/diretório.
f.is_dir() devolve True se for uma pasta, False se for ficheiro.
O == True é redundante, podias só escrever if f.is_dir():'''

'''Mostra no ecrã o nome da pasta (sem o caminho completo).
Se quisesses o caminho completo, podias usar f.path.'''

#exemplo de um caminho
'''/home/sonia_machado/
    projetos/
    imagens/
    notas.txt

    O programa vai imprimir:
    projetos
    imagens

Não imprime notas.txt, porque não é diretório.
Melhorando o código para imprimir  os ficheiros:
import os

dir_path = '/home/sonia_machado'

for f in os.scandir(dir_path):
    if f.is_dir():
        print("Pasta:", f.name)
    else:
        print("Ficheiro:", f.name)
'''

#Queres que eu te mostre como listar só os ficheiros Python (.py) dessa pasta
'''import os

dir_path = '/home/sonia_machado'

for f in os.scandir(dir_path):
    if f.is_file() and f.name.endswith(".py"):
        print("Ficheiro Python:", f.name)
        
#Se na tua pasta tiveres:
# variaveis.py
leitura_de_dados.py
documento.txt
imagens/

A saída será:
Ficheiro Python: variaveis.py
Ficheiro Python: leitura_de_dados.py

'''

#os.scandir(dir_path) é uma função do módulo os do Python.
#Recebe como argumento um caminho de pasta (dir_path).
#Devolve um iterador de objetos os.DirEntry.
'''Quando digo que os.scandir() devolve objetos ricos (DirEntry), quero dizer que não devolve apenas strings com os nomes dos ficheiros/pastas.
Exemplo com os.listdir()
import os
dir_path = '/home/sonia_machado'
for name in os.listdir(dir_path):
    print(name)
saída: 
variaveis.py
documento.txt
projetos
Aqui recebeste apenas strings. Não sabes se são pastas, ficheiros, nem tens o caminho completo

Exemplo com os.scandir()
import os
dir_path = '/home/sonia_machado'
for entry in os.scandir(dir_path):
    print(entry.name,#mostra o objeto 
    entry.is_file(),# True se for ficheiro
    entry.is_dir(),# True se for diretório
    entry.path, #caminho completo
    entry.name())# nome simples



Diferença para outras funções parecidas
os.listdir(path) → devolve só uma lista de nomes (strings).
os.scandir(path) → devolve objetos ricos (DirEntry) que já sabem se é ficheiro, diretório, caminho completo, etc.'''
#f.stat() devolve estatisticas(tamanhi, data de modificação, permissões, etc.)
# resultado do código em cima
'''<DirEntry 'variaveis.py'>
variaveis.py
/home/sonia_machado/variaveis.py
True
False

<DirEntry 'projetos'>
projetos
/home/sonia_machado/projetos
False
True
'''
#dirtentry: é uma classe interna do Pyhton que representa uma entrada num diretório (pasta).

'''Solicitar a path de uma pasta ao utilizador e comprimir todo o seu conteúdo através do código
que segue:'''
print('exercicio 7')
import shutil
import os.path
#creating the zip file
archieved=shutil.make_archive('meu_backup','zip','/home/sonia_machado/exer7.5')
#checking if the zip file exists
if os.path.exists(archieved):
    print('backup created successfully', archieved)
else:
    print('error creating backup')

