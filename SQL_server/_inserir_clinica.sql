USE Clinica;
GO

-------------------------
-- 1. Especialidades
-------------------------
INSERT INTO Especialidades (Nome)
VALUES
  ('Clínica Geral'),
  ('Cardiologia'),
  ('Dermatologia'),
  ('Ortopedia'),
  ('Pediatria');
GO

-------------------------
-- 2. Médicos
-------------------------
INSERT INTO Medicos (Nome, Email, Telefone)
VALUES
  ('Dr. João Silva',    'joao.silva@clinica.pt',   '910000001'),
  ('Dra. Maria Costa',  'maria.costa@clinica.pt', '910000002'),
  ('Dr. Pedro Sousa',   'pedro.sousa@clinica.pt', '910000003'),
  ('Dra. Ana Ramos',    'ana.ramos@clinica.pt',   '910000004');
GO

-------------------------
-- 3. Médicos x Especialidades
--   (associação muitos-para-muitos)
-------------------------
-- João: Clínica Geral e Cardiologia
INSERT INTO MedicoEspecialidade (IdMedico, IdEspecialidade)
VALUES
  (1, 1),
  (1, 2);

-- Maria: Dermatologia
INSERT INTO MedicoEspecialidade (IdMedico, IdEspecialidade)
VALUES
  (2, 3);

-- Pedro: Ortopedia
INSERT INTO MedicoEspecialidade (IdMedico, IdEspecialidade)
VALUES
  (3, 4);

-- Ana: Pediatria e Clínica Geral
INSERT INTO MedicoEspecialidade (IdMedico, IdEspecialidade)
VALUES
  (4, 5),
  (4, 1);
GO

-------------------------
-- 4. Pacientes
-------------------------
INSERT INTO Pacientes (Nome, Email, Cidade, DataRegisto)
VALUES
  ('Sofia Martins',  'sofia.martins@email.com',  'Lisboa',  '2024-01-10'),
  ('Carlos Ferreira','carlos.ferreira@email.com','Porto',   '2024-02-05'),
  ('Rita Gomes',     'rita.gomes@email.com',     'Braga',   '2024-03-18'),
  ('Miguel Alves',   'miguel.alves@email.com',   'Coimbra', '2024-04-22');
GO

-------------------------
-- 5. Exames (tipos de exame)
-------------------------
INSERT INTO Exames (Nome, Categoria, Preco)
VALUES
  ('Hemograma completo',         'Análises Clínicas', 15.00),
  ('Raio-X ao Tórax',            'Imagem',            40.00),
  ('Ecocardiograma',             'Cardiologia',       80.00),
  ('Ressonância Magnética Joelho','Imagem',          250.00),
  ('Teste de Alergias Cutâneas', 'Dermatologia',      60.00);
GO

-------------------------
-- 6. Consultas
-------------------------
INSERT INTO Consultas (IdPaciente, IdMedico, DataConsulta, MetodoPagamento)
VALUES
  (1, 1, '2024-05-10 10:00', 'Dinheiro'),
  (2, 2, '2024-05-11 15:30', 'Cartão'),
  (3, 3, '2024-05-12 09:15', 'Seguro'),
  (1, 4, '2024-06-01 11:00', 'Cartão'),
  (4, 1, '2024-06-05 16:45', 'Dinheiro');
GO

-------------------------
-- 7. Exames por Consulta
-------------------------
-- Consulta 1 (Sofia com Dr. João)
INSERT INTO ConsultaExames (IdConsulta, IdExame, Quantidade, PrecoUnitario)
VALUES
  (1, 1, 1, 15.00),   -- Hemograma
  (1, 3, 1, 80.00);   -- Ecocardiograma

-- Consulta 2 (Carlos com Dra. Maria)
INSERT INTO ConsultaExames (IdConsulta, IdExame, Quantidade, PrecoUnitario)
VALUES
  (2, 5, 1, 60.00);   -- Teste de alergias

-- Consulta 3 (Rita com Dr. Pedro)
INSERT INTO ConsultaExames (IdConsulta, IdExame, Quantidade, PrecoUnitario)
VALUES
  (3, 4, 1, 250.00);  -- RM Joelho

-- Consulta 4 (Sofia com Dra. Ana)
INSERT INTO ConsultaExames (IdConsulta, IdExame, Quantidade, PrecoUnitario)
VALUES
  (4, 1, 1, 15.00);   -- Hemograma

-- Consulta 5 (Miguel com Dr. João)
INSERT INTO ConsultaExames (IdConsulta, IdExame, Quantidade, PrecoUnitario)
VALUES
  (5, 2, 1, 40.00);   -- Raio-X Tórax
GO
