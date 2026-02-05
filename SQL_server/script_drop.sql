--DROP DATABASE TestDB;
--GO
--DROP DATABASE TestDB2;
--GO

---Para garantir que ninguém (nem o próprio VS Code) está a usar as bases de teste, use este script mais robusto:

--USE master;
--GO

-- Isto força a expulsão de qualquer utilizador da TestDB para permitir o DROP
--ALTER DATABASE TestDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
--GO
--DROP DATABASE TestDB;
--GO

-- Para garantir que ninguém (nem o próprio VS Code) está a usar as bases de teste, use este script mais robusto:
--USE master;
--GO

-- Isto força a expulsão de qualquer utilizador da TestDB para permitir o DROP
--ALTER DATABASE TestDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
--GO
--DROP DATABASE TestDB;
--GO

-- O mesmo para a TestDB2
ALTER DATABASE TestDB2 SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
GO
DROP DATABASE TestDB2;
GO