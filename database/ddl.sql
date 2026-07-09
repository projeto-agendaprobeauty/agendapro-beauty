
CREATE TABLE agenda
(
  id              serial      NOT NULL,
  status          varchar(10) NOT NULL,
  horario_inicio  time        NOT NULL,
  horario_fim     time        NOT NULL,
  data            date        NOT NULL,
  cliente_id      serial      NOT NULL,
  profissional_id serial      NOT NULL,
  servico_id      serial      NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE area
(
  id   serial      NOT NULL,
  nome varchar(20) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE cliente
(
  id       serial        NOT NULL,
  nome     varchar(30)   NOT NULL,
  email    varchar(40)   NOT NULL UNIQUE,
  telefone char(11) NOT NULL UNIQUE,
  PRIMARY KEY (id)
);

CREATE TABLE profissional
(
  id             serial      NOT NULL,
  nome           varchar(30) NOT NULL,
  email          varchar(40) NOT NULL UNIQUE,
  horario_inicio time        NOT NULL,
  horario_fim    time        NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE profissional_area
(
  area_id         serial NOT NULL,
  profissional_id serial NOT NULL,
  PRIMARY KEY (area_id, profissional_id)
);

CREATE TABLE profissional_servico
(
  profissional_id serial NOT NULL,
  servico_id      serial NOT NULL,
  PRIMARY KEY (profissional_id, servico_id)
);

CREATE TABLE servico
(
  id        serial       NOT NULL,
  nome      varchar(20)  NOT NULL,
  descricao varchar(200) NOT NULL,
  duracao   int     NOT NULL,
  preco     decimal(10,2) NOT NULL,
  area_id   serial        NOT NULL,
  PRIMARY KEY (id)
);

ALTER TABLE agenda
  ADD CONSTRAINT FK_cliente_TO_agenda
    FOREIGN KEY (cliente_id)
    REFERENCES cliente (id);

ALTER TABLE profissional_servico
  ADD CONSTRAINT FK_profissional_TO_profissional_servico
    FOREIGN KEY (profissional_id)
    REFERENCES profissional (id);

ALTER TABLE profissional_servico
  ADD CONSTRAINT FK_servico_TO_profissional_servico
    FOREIGN KEY (servico_id)
    REFERENCES servico (id);

ALTER TABLE profissional_area
  ADD CONSTRAINT FK_profissional_TO_profissional_area
    FOREIGN KEY (profissional_id)
    REFERENCES profissional (id);

ALTER TABLE profissional_area
  ADD CONSTRAINT FK_area_TO_profissional_area
    FOREIGN KEY (area_id)
    REFERENCES area(id);

ALTER TABLE agenda
  ADD CONSTRAINT FK_profissional_TO_agenda
    FOREIGN KEY (profissional_id)
    REFERENCES profissional (id);

ALTER TABLE agenda
  ADD CONSTRAINT FK_servico_TO_agenda
    FOREIGN KEY (servico_id)
    REFERENCES servico (id);

ALTER TABLE servico
  ADD CONSTRAINT FK_area_TO_servico
    FOREIGN KEY (area_id)
    REFERENCES area (id);