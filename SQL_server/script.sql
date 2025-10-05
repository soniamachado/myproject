CREATE DATABASE Loja;
GO

USE Loja;
GO

CREATE TABLE Produtos (
    id INT PRIMARY KEY,--id nome da coluna (int,pk-primary key)
    nome NVARCHAR(50),--nome nome da coluna, texto até 50 caracteresm compatível com acentos e carcateres especiais
    preco DECIMAL(10,2),--preço nome da coluna, número decimal com até 10 dígitos no total e 2 casa decimais.
    quantidade INT --quantidade nome da coluna, nºinteiro (150,200)
);
GO

INSERT INTO Produtos VALUES (1, 'Banana', 1.20, 150);
INSERT INTO Produtos VALUES (2, 'Laranja', 0.80, 200);
GO

--id(int,pk)   nome(NVARCHAR)   preco(DECIMAL)    quantidade(INT)
--1              Banana         1.2                 150
--2              Laranja        0.8                 200´




-- como crie a base de dados apenas usando a linha de comandos
-- USE TestDB2;
--2> BLE Inventory (id INT, name NVARCHAR(50), quantity INT);
--3> GO
--Changed database context to 'TestDB2'.
--1> INSERT INTO Inventory VALUES (1,'banana',150);
--2> INSERT INTO Inventory VALUES (2,'orange',154);
--3> GO

--como liguei ao meu sql
--sonia_machado@SniaMachado:~  $ docker start sql1
--Sonia_machado@SniaMachado:~  $ docker exec -it sql1 "bash"
--mssql@sql1:/$ /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "<palavra-passe>" -C -N