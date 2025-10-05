uSE Loja;
GO
--1.Para apagar toda a tabela e seus dados:
DROP Table dbo.Produtos;
GO
--Isso elimina completamente tanto a estrutura quanto todos os dados da tabela especifica
--2.Para apagar apenas o conteúdo(os registros), mantendo a tabela:
--DELETE FROM FRUTA;
--DELETE FROM PRODUTOS
--isso apaga todos os dados, mas mantém a tabela vazia.
--3.Apagar linhas específicas:
--DELETE FROM Fruta WHERE nome = 'Banana';

