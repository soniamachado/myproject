import pandas as pd

# Criar um DataFrame a partir de um dicionário
data = {
    "Nome": ["Ana", "Bruno", "Carla", "David"],
    "Idade": [23, 35, 29, 42],
    "Cidade": ["Lisboa", "Porto", "Coimbra", "Faro"]
}

df = pd.DataFrame(data)

#1-Mostrar o DataFrame com indicação do indice
print("DataFrame completo:")
print(df)

#2-Aceder a uma coluna apresentando o indice
print("\nColuna 'Nome':")# aparece Coluna 'Nome'
print(df["Nome"])

#3-Aceder a várias colunas, apresentando o indice
print("\nColunas 'Nome' e 'Idade':")
print(df[["Nome", "Idade"]])

#4-Aceder a uma linha pelo índice (linha 2 → Carla)
print("\nLinha pelo índice (loc):")
print(df.loc[2])  # índice = 2

#5-Aceder a um intervalo de linhas (as duas primeiras)
print("\nDuas primeiras linhas (iloc):")
print(df.iloc[0:2])

#6-Aceder a uma célula específica → idade de Carla
print("\nIdade da Carla:")
print(df.loc[2, "Idade"])

#7-Alterar índice para a coluna Nome
df_indexed = df.set_index("Nome")
print("\nDataFrame com 'Nome' como índice:")
print(df_indexed)

#8-Aceder à cidade do Bruno (agora pelo índice Nome)
print("\nCidade do Bruno:")
print(df_indexed.loc["Bruno", "Cidade"])

'''Valor obtido na console:
1-DataFrame completo:
    Nome  Idade   Cidade
0    Ana     23   Lisboa
1  Bruno     35    Porto
2  Carla     29  Coimbra
3  David     42     Faro

2-Coluna 'Nome':
0      Ana
1    Bruno
2    Carla
3    David

3-Colunas 'Nome' e 'Idade':
    Nome  Idade
0    Ana     23
1  Bruno     35
2  Carla     29
3  David     42

#print(df.loc[2]), devolver um panda.Series(coluna ou vector)
#quando se imprime uma Serie, o pandas mostra cada par índice->valor numa linha vertical
4-Linha pelo índice (loc):
Nome      Carla
Idade        29
Cidade   Coimbra

#se quisessemos ver a linha como uma tabela (DataFrame com 1linha
print(df.loc[[2]])) ou print(df.loc[2].to_fram().T)
resultad
         nome idade cidade
2       carla   29   coimbra

#print(df.iloc[0:2])
5-Duas primeiras linhas (iloc):
    Nome  Idade   Cidade
0    Ana     23   Lisboa
1  Bruno     35    Porto

#print(df.loc[2, "Idade"]). coluna ideade do indice 2, neste caso corresponde à carla
6-Idade da Carla:
29

#df_indexed = df.set_index("Nome") alterar o indice para a coluna nome
#print(df_indexed)
7-DataFrame com 'Nome' como índice:
       Idade   Cidade
Nome                  
Ana        23   Lisboa
Bruno      35    Porto
Carla      29  Coimbra
David      42     Faro

#print(df_indexed.loc["Bruno", "Cidade"]) aceder à coluna cidade do indice bruno
8-Cidade do Bruno:
Porto

loc usa rótulos do índice(se o +indice 0,1,2 então loc[2]é a terceira linha)
iloc usa posição inteira(posição 2=terceira linha)
df.iloc[2]   # devolve Series (terceira linha): impressão vertical (é normal).
df.iloc[[2]] # devolve DataFrame (terceira linha): impressão em tabela (horizontal).

'''