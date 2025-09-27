''''sugestão para anuncios: Pretende-se que seja implementado um programa em Python de forma que 
efetue a gestão da atividade diária de uma biblioteca.
biblioteca={
    'AAA-8-22-123456-7':{#ISBN(chave)}
    'titulo':'Nexus',
    'autor':'Yuval Noah Harari',
    'ano_publicacao': 2024,
    'genero':'disponivel',
    'emprestado_para':None,
    'data_emprestimo':None
    }}'''
'''menu:
1-Inserir livro
2-Eliminar livro
3-Atualizar livro
4-Emprestar livro
5-Devolver livro
6-Pesquisar livro
'''

import biblioteca
registo={}
while True: 
  print('Menu:')
  print("1-Inserir livro")
  print("2-Eliminar livro do repositório")
  print("3-Atualizar livro")
  print("4-Requisitar livro")
  print("5-Devolver livro")
  print("6-Pesquisar livro")
  opcao=int(input("Escolha uma opção:"))

  #Inserirlivro
  if(opcao==1):
    Lista=biblioteca.InserirLivro(registo) 
    biblioteca.lista_livros(Lista)
  #Eliminar livro
  elif(opcao==2):
    Eliminar=biblioteca.Eliminar (registo)
    
  #Atualizar livro
  elif(opcao==3):
    biblioteca.AtualizarLivro(registo)
  
  #Emprestar livro
  elif(opcao==4):
    biblioteca.RequisitarLivro(registo)

  #Devolver livro
  elif(opcao==5):
    biblioteca.DevolverLivro(registo) 

  #Pesquisar livro
  elif(opcao==6):
    biblioteca.PesquisarLivro(registo)
  else:
    break;        
