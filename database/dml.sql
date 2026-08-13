-- ==========================================
-- 1. INSERÇÃO NA TABELA: usuario (10 usuários no total)
-- ==========================================
INSERT INTO usuario (id, nome, senha, email, telefone) VALUES
-- Usuários híbridos (Cliente + Profissional)
(1, 'Mariana Silva', 'hash_mari', 'mariana.silva@salao.com', '11911111111'),
(2, 'Bruno Ramos', 'hash_bruno', 'bruno.ramos@salao.com', '11922222222'),
(3, 'Carla Dias', 'hash_carla', 'carla.dias@salao.com', '11933333333'),
-- Usuários apenas Clientes
(4, 'Juliana Costa', 'hash_ju', 'juliana.costa@email.com', '11944444444'),
(5, 'Ricardo Souza', 'hash_ricardo', 'ricardo.souza@email.com', '11955555555'),
(6, 'Fernanda Lima', 'hash_fer', 'fernanda.lima@email.com', '11966666666'),
(7, 'Lucas Oliveira', 'hash_lucas', 'lucas.oliveira@email.com', '11977777777'),
-- Usuários apenas Profissionais
(8, 'Rodrigo Hair', 'hash_rodrigo', 'rodrigo.hair@salao.com', '11988888888'),
(9, 'Gabriela Manicure', 'hash_gabi', 'gabi.unhas@salao.com', '11999999999'),
(10, 'Aline Estetica', 'hash_aline', 'aline.estetica@salao.com', '11900000000');


-- ==========================================
-- 2. INSERÇÃO NA TABELA: cliente
-- ==========================================
-- Usuários clientes: 1, 2, 3 (os híbridos) + 4, 5, 6, 7 (apenas clientes)
INSERT INTO cliente (id, usuario_id) VALUES
(1, 1), -- Mariana (Híbrida)
(2, 2), -- Bruno (Híbrido)
(3, 3), -- Carla (Híbrida)
(4, 4), -- Juliana
(5, 5), -- Ricardo
(6, 6), -- Fernanda
(7, 7); -- Lucas


-- ==========================================
-- 3. INSERÇÃO NA TABELA: profissional
-- ==========================================
-- Usuários profissionais: 1, 2, 3 (os híbridos) + 8, 9, 10 (apenas profissionais)
INSERT INTO profissional (id, horario_inicio, horario_fim, usuario_id) VALUES
(1, '09:00:00', '18:00:00', 1), -- Mariana (Híbrida)
(2, '09:00:00', '18:00:00', 2), -- Bruno (Híbrido)
(3, '10:00:00', '19:00:00', 3), -- Carla (Híbrida)
(4, '08:00:00', '17:00:00', 8), -- Rodrigo
(5, '09:00:00', '18:00:00', 9), -- Gabriela
(6, '10:00:00', '19:00:00', 10); -- Aline


-- ==========================================
-- 4. INSERÇÃO NA TABELA: area
-- ==========================================
INSERT INTO area (id, nome) VALUES
(1, 'Cabelo'),
(2, 'Manicure'),
(3, 'Maquiagem');


-- ==========================================
-- 5. INSERÇÃO NA TABELA: servico
-- ==========================================
INSERT INTO servico (id, nome, descricao, duracao, preco, area_id) VALUES
(1, 'Corte Feminino', 'Corte de cabelo feminino com lavagem inclusa.', 60, 120.00, 1),
(2, 'Pé e Mão', 'Serviço completo de manicure e pedicure.', 60, 70.00, 2),
(3, 'Maquiagem Social', 'Maquiagem para eventos e festas.', 90, 180.00, 3),
(4, 'Escova e Hidratação', 'Tratamento capilar com escovação.', 50, 95.00, 1),
(5, 'Alongamento em Gel', 'Alongamento de unhas técnica em gel.', 120, 150.00, 2);


-- ==========================================
-- 6. INSERÇÃO NA TABELA: profissional_area
-- ==========================================
INSERT INTO profissional_area (area_id, profissional_id) VALUES
(1, 1), -- Mariana trabalha com Cabelo
(1, 2), -- Bruno trabalha com Cabelo
(3, 3), -- Carla trabalha com Maquiagem
(1, 4), -- Rodrigo trabalha com Cabelo
(2, 5), -- Gabriela trabalha com Manicure
(3, 6); -- Aline trabalha com Maquiagem


-- ==========================================
-- 7. INSERÇÃO NA TABELA: profissional_servico
-- ==========================================
INSERT INTO profissional_servico (profissional_id, servico_id) VALUES
(1, 1), -- Mariana faz Corte Feminino
(1, 4), -- Mariana faz Escova
(2, 1), -- Bruno faz Corte Feminino
(3, 3), -- Carla faz Maquiagem Social
(4, 1), -- Rodrigo faz Corte Feminino
(4, 4), -- Rodrigo faz Escova
(5, 2), -- Gabriela faz Pé e Mão
(5, 5), -- Gabriela faz Alongamento em Gel
(6, 3); -- Aline faz Maquiagem Social


-- ==========================================
-- 8. INSERÇÃO NA TABELA: agenda
-- ==========================================
INSERT INTO agenda (status, horario_inicio, horario_fim, data, cliente_id, profissional_id, servico_id) VALUES
-- Clientes normais agendando com profissionais
('Confirmado', '10:00:00', '11:00:00', '2026-08-20', 4, 4, 1), -- Juliana (cliente 4) com Rodrigo (prof 4) para Corte
('Confirmado', '14:00:00', '15:00:00', '2026-08-20', 5, 5, 2), -- Ricardo (cliente 5) com Gabriela (prof 5) para Pé e Mão
('Pendente',   '11:00:00', '12:30:00', '2026-08-21', 6, 6, 3), -- Fernanda (cliente 6) com Aline (prof 6) para Maquiagem

-- Clientes que também são profissionais agendando serviços no salão
('Confirmado', '09:00:00', '10:00:00', '2026-08-22', 1, 5, 2), -- Mariana (cliente 1) agendou Pé e Mão com Gabriela (prof 5)
('Pendente',   '16:00:00', '17:00:00', '2026-08-22', 2, 1, 4); -- Bruno (cliente 2) agendou Escova com Mariana (prof 1)