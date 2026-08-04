CREATE VIEW usuario_cliente AS
SELECT u.id AS usuario_id, c.id AS cliente_id, nome, senha, email, telefone FROM cliente c 
JOIN usuario u ON c.usuario_id = u.id ;

CREATE VIEW usuario_profissional AS
SELECT u.id AS usuario_id, p.id AS profissional_id, nome, senha, email, telefone FROM profissional p 
JOIN usuario u ON p.usuario_id = u.id ;

CREATE VIEW servico_status AS
SELECT a.id AS agenda_id, s.id as servico_id, status, data, nome, descricao FROM agenda a 
JOIN servico s ON a.id = s.id;