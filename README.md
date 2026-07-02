# AgendaPro-Beauty

Status do Projeto: Em desenvolvimento (Residência Técnica)

O AgendaPro-Beauty é a simulação de uma demanda real de mercado: a digitalização do sistema de agendamentos de um salão de beleza. O objetivo é substituir o processo manual (feito via WhatsApp ou telefone) por uma solução automatizada, eliminando conflitos de horários, retrabalho e a falta de controle gerencial.

---

## Objetivos de Aprendizado

Ao final deste desafio, os participantes estarão aptos a:

- **Desenvolvimento Full-Stack:** Construir uma aplicação web completa com autenticação e controle de acesso.
- **Regras de Negócio Complexas:** Implementar sistemas de agendamento com regras estritas de disponibilidade.
- **Integração:** Criar e consumir APIs REST para conectar o Front-end ao Back-end.
- **Banco de Dados:** Modelar e estruturar bancos de dados relacionais eficientes.
- **Boas Práticas:** Organizar, documentar e versionar código seguindo padrões de mercado.
- **Metodologia Ágil:** Trabalhar em equipe utilizando frameworks ágeis e demonstrar evolução técnica contínua.

---

## Escopo do Sistema (Visão do MVP)

### Funcionalidades para o Cliente

- **Acesso:** Cadastro e login de usuários.
- **Catálogo:** Visualização de serviços oferecidos e profissionais disponíveis.
- **Busca Inteligente:** Filtros por área do salão (Cabelo, Manicure, Estética Facial, Corporal, etc.).
- **Agendamento:** Escolha de data/horário disponíveis e confirmação automática.
- **Autonomia:** Cancelamento ou reagendamento dentro das regras definidas.

### Funcionalidades Administrativas

- **Cadastros:** Gerenciamento de profissionais, serviços (com duração e valor) e áreas do salão.
- **Gestão de Escala:** Definição de horários de trabalho por profissional e bloqueio manual de horários.
- **Visualização:** Agenda completa organizada por profissional.
- **Dashboard Gerencial:**
  - Total de agendamentos realizados.
  - Serviços mais solicitados.
  - Profissionais mais requisitados.

### Regras de Negócio do MVP

> **Importante:** O sistema deve impedir rigorosamente o conflito de horários, considerando o tempo de duração de cada serviço para bloquear a agenda automaticamente.

- **Cancelamento:** Permitido apenas com uma antecedência mínima configurável.
- **Fluxo de Status:** Controle rigoroso dos estados do agendamento (Confirmado, Cancelado, Concluído).
- **Segurança:** Persistência em banco de dados relacional com controle básico de segurança e autenticação.

---

## Divisão de Responsabilidades

Para o desenvolvimento do projeto, a equipe foi dividida em duas grandes frentes:

### Front-end

- Desenvolvimento da interface pública e responsiva do site.
- Criação de uma tela de agendamento intuitiva para o cliente.
- Construção da interface administrativa (painel interno).
- Foco na experiência do usuário (UX/UI) para clientes e administradores.
- Consumo da API REST e validação de dados no lado do cliente.

### Back-end

- Modelagem do banco de dados relacional.
- Implementação das regras de negócio de agendamento e disponibilidade.
- Criação e estruturação da API REST.
- Controle de autenticação, autorização e segurança dos dados.
- Gestão e lógica de mudança de status dos agendamentos.

---

## Tecnologias Sugeridas

| Camada             | Tecnologias Recomendadas                           |
| :----------------- | :------------------------------------------------- |
| **Front-end**      | React, Vue.js ou HTML5 / CSS3 / JavaScript Vanilla |
| **Back-end**       | Python                                             |
| **Banco de Dados** | PostgreSQL ou MySQL                                |
| **Versionamento**  | Git e GitHub                                       |
| **Metodologia**    | Scrum ou Kanban                                    |

---

## Resultado Esperado (Final de 3 Meses)

Ao encerramento da residência, os seguintes artefatos devem ser entregues:

1. **Sistema Funcional:** Aplicação rodando de ponta a ponta (MVP).
2. **Código Organizado:** Repositório limpo, versionado e seguindo boas práticas de Git.
3. **Documentação:** Este README.md atualizado com as instruções de instalação + documentação clara da API.
