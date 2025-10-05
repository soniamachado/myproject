USE Loja;
GO

EXEC sp_rename 'Produtos', 'Fruta';
GO

-- Depois, faça os INSERTS se a estrutura da tabela for igual.
INSERT INTO Fruta VALUES (1, 'Banana', 1.20, 150);
INSERT INTO Fruta VALUES (2, 'Laranja', 0.80, 200);
GO
