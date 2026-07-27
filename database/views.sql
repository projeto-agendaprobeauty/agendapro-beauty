CREATE VIEW usuario_cliente AS
SELECT u.id AS usuario_id, c.id AS cliente_id, nome, senha, email, telefone FROM cliente c 
JOIN usuario u ON c.usuario_id = u.id ;

CREATE VIEW usuario_profissional AS
SELECT u.id AS usuario_id, p.id AS profissional_id, nome, senha, email, telefone FROM profissional p 
JOIN usuario u ON p.usuario_id = u.id ;