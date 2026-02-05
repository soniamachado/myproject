-- Criar base de dados
CREATE DATABASE Clinica;
GO

USE Clinica;
GO


-- Tabela de Pacientes (equivalente a Clientes)
CREATE TABLE Pacientes (
    IdPaciente       INT IDENTITY(1,1) PRIMARY KEY,
    Nome             NVARCHAR(100)   NOT NULL,
    Email            NVARCHAR(150)   NULL,
    Cidade           NVARCHAR(80)    NULL,
    DataRegisto      DATE            NOT NULL DEFAULT (GETDATE())
);
GO

-- Tabela de Médicos
CREATE TABLE Medicos (
    IdMedico         INT IDENTITY(1,1) PRIMARY KEY,
    Nome             NVARCHAR(100)   NOT NULL,
    Email            NVARCHAR(150)   NULL,
    Telefone         NVARCHAR(20)    NULL
);
GO

-- Tabela de Especialidades
CREATE TABLE Especialidades (
    IdEspecialidade  INT IDENTITY(1,1) PRIMARY KEY,
    Nome             NVARCHAR(100) NOT NULL
);
GO

-- Relação Médico–Especialidade (um médico pode ter várias especialidades)
CREATE TABLE MedicoEspecialidade (
    IdMedico         INT NOT NULL,
    IdEspecialidade  INT NOT NULL,
    CONSTRAINT PK_MedicoEspecialidade PRIMARY KEY (IdMedico, IdEspecialidade),
    CONSTRAINT FK_MedicoEspecialidade_Medico
        FOREIGN KEY (IdMedico) REFERENCES Medicos(IdMedico),
    CONSTRAINT FK_MedicoEspecialidade_Especialidade
        FOREIGN KEY (IdEspecialidade) REFERENCES Especialidades(IdEspecialidade)
);
GO

-- Tabela de Consultas (equivalente a Encomendas)
CREATE TABLE Consultas (
    IdConsulta       INT IDENTITY(1,1) PRIMARY KEY,
    IdPaciente       INT NOT NULL,
    IdMedico         INT NOT NULL,
    DataConsulta     DATETIME2       NOT NULL,
    MetodoPagamento  NVARCHAR(30)    NULL,   -- Ex.: Dinheiro, Cartão, Seguro
    CONSTRAINT FK_Consultas_Paciente
        FOREIGN KEY (IdPaciente) REFERENCES Pacientes(IdPaciente),
    CONSTRAINT FK_Consultas_Medico
        FOREIGN KEY (IdMedico) REFERENCES Medicos(IdMedico)
);
GO

-- Tabela de Tipos de Exame (equivalente a Produtos)
CREATE TABLE Exames (
    IdExame          INT IDENTITY(1,1) PRIMARY KEY,
    Nome             NVARCHAR(120)   NOT NULL,
    Categoria        NVARCHAR(80)    NULL,   -- Ex.: Sangue, Imagem, etc.
    Preco            DECIMAL(10,2)   NOT NULL
);
GO

-- Tabela de Exames marcados em cada consulta (equivalente a EncomendaItens)
CREATE TABLE ConsultaExames (
    IdConsulta       INT NOT NULL,
    IdExame          INT NOT NULL,
    Quantidade       INT NOT NULL DEFAULT 1,
    PrecoUnitario    DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_ConsultaExames PRIMARY KEY (IdConsulta, IdExame),
    CONSTRAINT FK_ConsultaExames_Consulta
        FOREIGN KEY (IdConsulta) REFERENCES Consultas(IdConsulta),
    CONSTRAINT FK_ConsultaExames_Exame
        FOREIGN KEY (IdExame) REFERENCES Exames(IdExame)
);
GO
