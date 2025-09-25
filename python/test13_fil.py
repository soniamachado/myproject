paises =[]

with open('/home/sonia_machado/myproject/python/samples.txt', 'r') as f:
    for linha in f:
        linha = linha.strip()  # remover espaços e \n no fim
        if not linha:
            continue  # salta linhas vazias

        lista_campos = linha.split()  # dividir por espaços/tabs se a linha for "Afghanistan;+93", então a lista_campos será ['Afghanistan', '+93']
        paises.append(lista_campos[0])  # guardar o nome do país (primeiro campo)

        if lista_campos[0] == 'Afghanistan':
            print('País:', lista_campos[0])
            print('Indicativo:', lista_campos[1])

# ordenar lista de países
print('Países ordenados alfabeticamente:')
paises.sort()
print(paises)
'''ficheiro1.txt
Afghanistan;+93
Portugal;+351
Brazil;+55
Spain;+34

a saída será:
País: Afghanistan
Indicativo: +93
Países ordenados alfabeticamente:
['Afghanistan', 'Brazil', 'Portugal', 'Spain']'''
#quando copiaste o ficheiro para a pasta do repositório, aparecem dois ficheiros, o ficheiro que tu queres-samples.txt e o samples.txt~ que é uma cópia de segurança que o editor faz automaticamente. Se quiseres apagar esse ficheiro, podes apagá-lo sem problemas.
#isto é um alternate data stream(ADS) criado pelo windows.
'''EXPLICAÇÃO No Windows, quando descarregas/copias ficheiros da Internet, o sistema cria esse Zone.Identifier para marcar que o ficheiro veio da Internet.
É uma "marca de segurança" usada pelo Windows SmartScreen e pelo Internet Explorer/Edge.
Não é código, é só metadados.

O que é a pasta __pycache__/

É uma pasta criada automaticamente pelo Python.

Sempre que corres um ficheiro Python (.py), o Python compila-o para um formato mais rápido (.pyc) e guarda dentro de __pycache__/.

Tu não precisas criar nem apagar → o Python trata disso sozinho.

Exemplo:

meu_script.py
__pycache__/
   └── meu_script.cpython-311.pyc
📌 Porque aparece numa pasta e noutra não?
Se corres python meu_script.py → o Python normalmente cria o __pycache__/.
Mas pode não aparecer se:
O código é muito pequeno/simples (Python decide não guardar .pyc).
O ambiente tem a cache desativada (com a variável de ambiente PYTHONDONTWRITEBYTECODE=1).
Usaste uma IDE (tipo VS Code ou PyCharm) que executa em modo sem cache.
Já apagaste manualmente.
Ou seja: não é obrigatório aparecer sempre.


O que o .gitignore faz

Se criares um ficheiro/pasta que esteja listado no .gitignore, o Git finge que não existe.

Ou seja, não aparece no git status, não vai para git add, nem para commits.

Mas o ficheiro continua no teu disco normalmente.
'''