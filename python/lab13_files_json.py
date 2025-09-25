#quando eu rodar este ficheiro, ele cria um ficheiro disciplinas.json na mesma pasta
#o json é um formato de ficheiro muito usado para guardar dados estruturados, como listas ou dicionários
#é um formato leve, fácil de ler e escrever, e é amplamente suportado por várias linguagens de programação
#neste exemplo, criar um programa que permita gerir uma lista de disciplinas com as respetivas notas
#o programa deve permitir inserir, atualizar, eliminar e listar disciplinas
#as disciplinas e notas devem ser guardadas num ficheiro JSON para que os dados persistam
'''JSON (JavaScript Object Notation) é um formato leve de troca de dados, fácil de ler e escrever para humanos,
 e fácil de analisar e gerar para máquinas. É amplamente utilizado para armazenar e
   transmitir dados entre um servidor e uma aplicação web, ou entre diferentes sistemas.
   Muito usado em APIs(application programming interfaces servem para comunicar entre programas pela internet), configuração, e armazenamento leve de informação.'''
import json
import os # não é uma função, é um módulo  de bibilioteca padrão do Python que fornece funções para interagir com o sistema operativo, como manipulação de ficheiros e diretórios

FICHEIRO_JSON = "disciplinas.json"

# Função para carregar disciplinas do ficheiro/guardar no ficheiro JSON
'''exemplo do dicionario que vamos guardar no ficheiro JSON:
disciplinas = {
    "Matemática": 15.5,
    "Português": 14,
    "História": 12
}
with open("notas.json", "r") as f:
    disciplinas = json.load(f)

print(disciplinas)
# {'Matemática': 15.5, 'Português': 14, 'História': 12}
criamos um ficheiro com código em cima
'''
def carregar_disciplinas():
    if os.path.exists(FICHEIRO_JSON):#verifica se o ficheiro existe no disco.FICHEIRO_JSON é só uma variável com nome do ficheiro
        with open(FICHEIRO_JSON, "r") as f:#com o r trata-se de modo de leitura
            return json.load(f) #devolve o dicionário 
    return {} # se não existir, devolve o vazio
'''versão direta(sem função)
import os
if os.path.exists("disciplinas.json"):
    with open("disciplinas.json", "r") as f:
        disciplinas = json.load(f)
        else:
            disciplinas = {}
            
Quando usas .json() no Python, isto transforma-se num dicionário:'''

# Função para guardar disciplinas no ficheiro
def guardar_disciplinas(disciplinas):
    with open(FICHEIRO_JSON, "w") as f:
        json.dump(disciplinas, f, indent=4)#indent=4 para ficar bonito, trata-se de indentacao
#Quando usas .json() no Python, isto transforma-se num dicionário:
#para guardar o dicionário num ficheiro JSON, usamos json.dump()

'''com ident=4 o ficheiro JSON fica assim: mesmo que seja 2 ou 200 chaves, apenas diz como mostrar cada linha no ficheiro JSON
 {
    "Matemática": 15.5,
    "Português": 14,
    "História": 12,
    "Biologia": 18
}
import json

with open("notas.json", "w") as f:
    json.dump(disciplinas, f, indent=4)  # indent=4 para ficar bonito
só com este código cria um ficheiro notas.json com o conteúdo do dicionário disciplinas
#para guardar o dicionário num ficheiro JSON, usamos json.dump()'''
# Funções para gerir disciplinas
def listar_disciplinas(disciplinas):
    if not disciplinas:
        print("Nenhuma disciplina inserida.")
        return
    print("\nDisciplinas:")
    for chave, valor in disciplinas.items():
        print(f"- {chave}: {valor}")

def inserir_disciplina(disciplinas):
    nome = input("Introduzir disciplina: ").strip()
    if nome in disciplinas:
        print("Disciplina já existe.")
        return
    try:
        nota = float(input("Introduzir nota: "))
        disciplinas[nome] = nota
        guardar_disciplinas(disciplinas)
        print("Disciplina adicionada com sucesso.")
    except ValueError:
        print("Nota inválida, deve ser um número.")

def atualizar_disciplina(disciplinas):
    nome = input("Disciplina a atualizar: ").strip()
    if nome not in disciplinas:
        print("Disciplina não encontrada.")
        return
    try:
        nota = float(input("Nova nota: "))
        disciplinas[nome] = nota
        guardar_disciplinas(disciplinas)
        print("Disciplina atualizada com sucesso.")
    except ValueError:
        print("Nota inválida, deve ser um número.")

def eliminar_disciplina(disciplinas):
    nome = input("Disciplina a eliminar: ").strip()
    if nome in disciplinas:
        del disciplinas[nome]
        guardar_disciplinas(disciplinas)
        print("Disciplina eliminada com sucesso.")
    else:
        print("Disciplina não encontrada.")

# Programa principal
disciplinas = carregar_disciplinas()

while True:
    print("\n1 - Inserir disciplina")
    print("2 - Atualizar disciplina")
    print("3 - Eliminar disciplina")
    print("4 - Listar disciplinas")
    print("5 - Sair")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        inserir_disciplina(disciplinas)
    elif opcao == "2":
        atualizar_disciplina(disciplinas)
    elif opcao == "3":
        eliminar_disciplina(disciplinas)
    elif opcao == "4":
        listar_disciplinas(disciplinas)
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")

#outros módulos os 
'''
1.listar ficheiros numa pasta
import os
print(os.listdir('.')) # lista ficheiros na pasta atual

2.criar uma pasta
os.mkdir('minha_pasta')

3.descobrir a pasta atual
print(os.getcwd()) # mostra a pasta atual'''