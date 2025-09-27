'''biblioteca={
    'AAA-8-22-123456-7':{#ISBN(chave)}
    'titulo':'Nexus',
    'autor':'Yuval Noah Harari',
    'ano_publicacao': 2024,
    'genero':'disponivel',
    'emprestado_para':None,
    'data_emprestimo':None
    }}
    Opção'''
#Principais requisitos a implementar neste desenvolvimento:

'''✓ optar pela utilização de uma coleção de dados
✓ implementar uma função para cada opção do menu
✓ utilizar um módulo para a implementação das funções
✓ sempre que possível utilizar o tratamento de erros
✓ definir um formato para o ISBN e sempre que necessário efetuar a validação
✓ validar o ano introduzido (por exemplo, para evitar valores negativos)
✓ todas as datas escritas no terminal, devem apresentar a seguinte máscara:
dd/mm/yyyy'''
def ajustar_data(dataEmprestimo):
    #remove espaços em branco e subistitui outros separadores por "/"
    data=dataEmprestimo.strip().replace('-','/').replace('.', '/').replace(' ', '/')
    #divide a data em partes(dia, mês, ano)
    partes=data.split('/')
    #garante que tmeos exatamente em 3 partes
    if len(partes)==3:
        dia, mes, ano=partes
        #ajusta os valores para garantir que são válidos
        dia=dia.zfill(2)#adicionar um zero à esquerda
        mes=mes.zfill(2)
        ano=ano.zfill(4) if len(ano)<=4 else ano[:4] #garante ano de 4 dígitos
        '''mesmo em cima que colocar:
        if len(ano)<=4
            ano=ano.zfill(4)
        else:
            print(ano)'''
        #retorna a data formatada
        return f'{dia}/{mes}/{ano}'
    else:
        return 'Data inválida'
    
def lista_livros(registo):
    for codigo, categoria in registo.items():
        print(f'Código:{codigo}')
        for categoria, valor in categoria.items():
            print( f'{categoria}:{valor}') #exibe as vategorias e os seus valores
        print() #adiciona uma linha em branco para separar os livros


def InserirLivro(registo):
    try:
        while True:
            novo_livro=input('Coloque o código do livro de acordo com a seguinte referência "AAA-8-22-123456-7":')
            if len(novo_livro)!=17:
                print('Digitou errado')
                continue
            
            verficar_se_existe=registo.get(novo_livro)
            if verficar_se_existe is None:
                titulo=input('Insire o título:')
                autor=input('Insire o autor:')
                anoPublicado=int(input('Coloque a data de publicação:'))
                numero_disponivel=int(input('Quantidade de livros a adicionar na biblioteca:'))
                nomeRequisitor=input('Insira o nome da pessoa que requesitou o livro:')
                dataEmprestimo=input('Digite a data de emprestimo:')
                dataCorrigida=ajustar_data(dataEmprestimo)
                registo[novo_livro]={
                    'titulo': titulo,
                    'autor': autor,
                    'anoPublicado': anoPublicado,
                    'numero_disponivel':numero_disponivel,
                    'nomeRequisitor': nomeRequisitor or None,
                    'DataEmprestimo': dataCorrigida or None
                }
                print('Livro adicionado com sucesso')
                return registo
            else:
                print('ID já cadastrado! Por favor, escolha outro ')
                #adiciona    r quantidade de livros ao existentes
                break
    except ValueError:
        print('Erro: Ano de publicação e número de livros devem ser número inteiros ')
            #escrever função do dicionário
    except Exception as e:
        print(f'Erro ao inserir livro: {str(e)}')
    return registo
    
def Eliminar(registo):
    print('Escolheu eliminar repositório')
    eliminarLivro=input('Qual o livro que quer eliminar, insira o código')
    if(eliminarLivro in registo):
        del registo[eliminarLivro]
        print(f'Livro com o código "{eliminarLivro}" foi removido do registro.')
    else:
        print(f'Livro com o código "{eliminarLivro}" não encontrado para remoção.')


    
def AtualizarLivro(registo):
    try:
        print('Atualizar repositório...')
        livro_atualizado=input('Introduzir código do livro:')
        verificar_se_existe=registo.get(livro_atualizado)
        if verificar_se_existe is not None:
            print('Livro encontrado! Detalhes atuais:')
            atualizado=False
            for categoria, valor in verificar_se_existe.items():
                print(f'{categoria}:{valor}')

            categoria=input('qual a categoria que gostava de utilizar?')
            if categoria in verificar_se_existe:    
                novo_valor=input(f'Insire o novo valor para {categoria}:')
                registo[livro_atualizado][categoria]=[novo_valor]
                atualizado==True
                
        if atualizado==True:
            print('Livro atualizado com sucesso')
        else:
            print('Livro não encontrado para atualização')
        return registo #retorna o registro atualizado
    except Exception as e:
        print('erro ao tentar atualizar o livro:', str(e))# vai me indicar que tipo de erro consiste 
        #e é o objeto da exceção que foi capturada, stre(e) converte a mensagem
        return registo #retorna o registo mesmo em caso de erro

def RequisitarLivro(registo):
    try:
        print('=== Requisitar Livro ===')
        
        # Solicitar o código do livro a requisitar
        livro_requisitado = input('Digite o código do livro que deseja requisitar: ')
        
        # Verificar se o livro existe no registro
        if livro_requisitado in registo:
            # Exibir detalhes do livro antes de requisitar
            print(f'Detalhes do livro requisitado: {registo[livro_requisitado]}')
            
            confirmar = input('Tem certeza de que deseja requisitar este livro? (s/n): ').lower()
            if confirmar == 's':
                # Chama a função Eliminar para remover o livro
                Eliminar(registo, livro_requisitado)
                print(f'Livro com o código "{livro_requisitado}" requisitado e removido com sucesso.')
            else:
                print('Ação de requisição cancelada.')
        else:
            print(f'Livro com o código "{livro_requisitado}" não encontrado no registro.')
    
    except Exception as e:
        print(f'Erro ao tentar requisitar o livro: {str(e)}')


def DevolverLivro(registo):
    try:
        print('=== Entregar Livro ===')
        # Solicitar o código do livro entregue
        codigo_livro = input('Digite o código do livro que deseja entregar: ')
        
        # Verificar se o livro já existe no registro
        if codigo_livro in registo:
            # Atualizar o número de exemplares disponíveis
            numero_atual = registo[codigo_livro]['numero_disponivel']
            registo[codigo_livro]['numero_disponivel'] = numero_atual + 1

            print(f'Livro com o código "{codigo_livro}" atualizado: número de exemplares disponíveis agora é {registo[codigo_livro]["numero_disponivel"]}.')
        else:
            # Chamar a função InserirLivro para adicionar o livro ao registro
            print(f'Livro com o código "{codigo_livro}" não encontrado no registro. Adicionando como um novo livro.')
            InserirLivro(registo)  # Reutiliza a função InserirLivro para gerenciar a adição do novo livro.
    
    except Exception as e:
        print(f'Erro ao tentar entregar o livro: {str(e)}')


def PesquisarLivro(registo):
    try:
        # Solicitar o código do livro
        codigo = input('Insira o código do livro: ')
        
        # Verificar se o código existe no registro
        livro = registo.get(codigo)
        if livro in registo:
            print(f'Livro encontrado: Código: {codigo} \n')
            for categoria, valor in livro.items():
                print(f'{categoria}: {valor}')
        else:
            print('Livro não encontrado com esse código.')
    except Exception as e:
        print(f'Ocorreu um erro ao pesquisar o livro: {str(e)}')