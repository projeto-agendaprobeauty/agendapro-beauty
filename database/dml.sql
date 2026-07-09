-- ==========================
-- ÁREAS
-- ==========================
INSERT INTO area (nome) VALUES
('Cabelo'),
('Estética'),
('Barbearia'),
('Manicure');

-- ==========================
-- CLIENTES
-- ==========================
INSERT INTO cliente (nome, email, telefone) VALUES
('João Silva', 'joao@email.com', '11999990001'),
('Maria Oliveira', 'maria@email.com', '11999990002'),
('Pedro Santos', 'pedro@email.com', '11999990003'),
('Ana Costa', 'ana@email.com', '11999990004'),
('Lucas Lima', 'lucas@email.com', '11999990005');

-- ==========================
-- PROFISSIONAIS
-- ==========================
INSERT INTO profissional
(nome, email, horario_inicio, horario_fim)
VALUES
('Carlos Mendes', 'carlos@salon.com', '08:00', '17:00'),
('Fernanda Rocha', 'fernanda@salon.com', '09:00', '18:00'),
('Juliana Alves', 'juliana@salon.com', '10:00', '19:00');

-- ==========================
-- SERVIÇOS
-- ==========================
INSERT INTO servico
(nome, descricao, duracao, preco, area_id)
VALUES
('Corte Masculino', 'Corte tradicional masculino', 40, 45.00, 3),
('Corte Feminino', 'Corte feminino personalizado', 60, 80.00, 1),
('Escova', 'Escova simples', 40, 50.00, 1),
('Coloração', 'Coloração completa', 120, 180.00, 1),
('Manicure', 'Manicure completa', 45, 35.00, 4),
('Pedicure', 'Pedicure completa', 50, 40.00, 4),
('Limpeza de Pele', 'Limpeza facial profunda', 90, 150.00, 2);

-- ==========================
-- PROFISSIONAL x ÁREA
-- ==========================
INSERT INTO profissional_area
(area_id, profissional_id)
VALUES
(1,1),
(3,1),
(2,2),
(4,3);

-- ==========================
-- PROFISSIONAL x SERVIÇO
-- ==========================
INSERT INTO profissional_servico
(profissional_id, servico_id)
VALUES
(1,1),
(1,2),
(1,3),
(2,4),
(2,7),
(3,5),
(3,6);

-- ==========================
-- AGENDAMENTOS
-- ==========================
INSERT INTO agenda
(status, horario_inicio, horario_fim, data, cliente_id, profissional_id, servico_id)
VALUES
('Marcado', '08:00', '08:40', '2026-07-10', 1, 1, 1),
('Marcado', '09:00', '10:00', '2026-07-10', 2, 1, 2),
('Concluido', '10:30', '11:10', '2026-07-09', 3, 1, 3),
('Marcado', '09:00', '11:00', '2026-07-11', 4, 2, 4),
('Concluido', '14:00', '15:30', '2026-07-08', 5, 2, 7),
('Marcado', '10:00', '10:45', '2026-07-12', 2, 3, 5),
('Cancelado', '11:00', '11:50', '2026-07-12', 1, 3, 6);