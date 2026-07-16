import os
from fastapi import APIRouter
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

print("Diretório atual:", os.getcwd())
print("DATABASE_URL:", os.getenv("DATABASE_URL"))


DATABASE_URL = os.getenv('DATABASE_URL')

router = APIRouter(prefix='/agenda', tags=['Agenda'])
from classes.agenda import Agenda

engine = create_engine(DATABASE_URL)

#Create
@router.post('')
def cadastrar_agendamento(agenda :Agenda):
    try:
        with engine.begin() as con:
            sql = """SELECT duracao FROM servico WHERE id = :id_servico"""
            response = con.execute(sql, {"id_servico" : agenda.servico_id})     
            sql = """INSERT INTO public.agenda 
                    (status, horario_inicio, horario_fim, data, cliente_id, profissional_id, servico_id)
                VALUES ( :status, :horario_inicial, :horario_final, :data, :cliente_id, :profissional_id, :servico_id)"""            
            dados = {
                "status": agenda.status,
                "horario_inicial": agenda.horario_inicial,
                "horario_final": agenda.horario_final,
                "data": agenda.data,
                "cliente_id": agenda.cliente_id,
                "profissional_id": agenda.profissional_id,
                "servico_id": agenda.servico_id
            }

            resultado = con.execute(text(sql), dados)
            print("Linhas afetadas:", resultado.rowcount)

    except Exception as erro:
        print("ERRO:", erro)
        return {"erro": str(erro)}
        
    engine.dispose()
    return 'Agendamento cadastrado com sucesso!'

# Read (todos os agendamentos)
@router.get('')
def listar_agendamentos():
    try:
        with engine.connect() as con:
            # AO INVÉS DE EXIBIR OS IDS, EXIBE OS NOMES DO PROFISSIONAL, CLIENTE E DO SERVIÇO
            sql = """SELECT a.id, a.cliente_id, cliente.nome as cliente_nome, a.servico_id, servico.nome as servico_nome, a.profissional_id, profissional.nome as profissional_nome, data, a.horario_inicio, a.horario_fim, status
                    FROM agenda a JOIN cliente ON a.cliente_id = cliente.id 
                    JOIN profissional ON a.profissional_id = profissional.id
                    join servico ON a.servico_id = servico.id
					ORDER BY data ASC;"""
            response = con.execute(text(sql))
            result = []
            for row in response:
                linha = row._mapping
                agenda = {
                    linha['id']: {
                        "cliente": {
                            "id": linha['cliente_id'],
                            "nome": linha['cliente_nome']
                        },
                        "servico": {
                            "id": linha['servico_id'],
                            "nome": linha['servico_nome']
                        },
                        "profissional": {
                            "id": linha['profissional_id'],
                            "nome": linha['profissional_nome']
                        },
                        "inicio": linha['horario_inicio'],
                        "fim": linha['horario_fim'],
                        "status": linha['status']
                    }
                }
                result.append(agenda)
    except Exception as e:
        return e
    engine.dispose()
    return result

# Read (buscar agendamento por id)
@router.get('/{id}')
def buscar_agendamento(id : int):

    
    try:
        with engine.connect() as con:
            sql = """SELECT a.id, a.cliente_id, cliente.nome as cliente_nome, a.servico_id, servico.nome as servico_nome, a.profissional_id, profissional.nome as profissional_nome, data, a.horario_inicio, a.horario_fim, status
                    FROM agenda a JOIN cliente ON a.cliente_id = cliente.id 
                    JOIN profissional ON a.profissional_id = profissional.id
                    join servico ON a.servico_id = servico.id
                    WHERE a.id = :id
					ORDER BY data ASC;"""
            response = con.execute(text(sql), {"id": id})
            row = response.fetchone()
            linha = row._mapping
            result = {
                    "cliente": {
                        "id": linha['cliente_id'],
                        "nome": linha['cliente_nome']
                    },
                    "servico": {
                        "id": linha['servico_id'],
                        "nome": linha['servico_nome']
                    },
                    "profissional": {
                        "id": linha['profissional_id'],
                        "nome": linha['profissional_nome']
                    },
                    "inicio": linha['horario_inicio'],
                    "fim": linha['horario_fim'],
                    "status": linha['status']
            }
    except Exception as e:
        return e
    engine.dispose()
    return result
    
@router.put('/{id}')
def atualizar_agendamento(id: int, agenda :Agenda):
    
    try:
        with engine.begin() as con: 
            sql = """UPDATE public.agenda
                    SET status = :status,
                        horario_inicio = :horario_inicial,
                        horario_fim = :horario_final,
                        data = :data,
                        cliente_id = :cliente_id,
                        profissional_id = :profissional_id,
                        servico_id = :servico_id
                    WHERE id = :id"""
            dados = {
                "id": id,
                "status": agenda.status,
                "horario_inicial": agenda.horario_inicial,
                "horario_final": agenda.horario_final,
                "data": agenda.data,
                "cliente_id": agenda.cliente_id,
                "profissional_id": agenda.profissional_id,
                "servico_id": agenda.servico_id
            }
            con.execute(text(sql), dados)
    except Exception as erro:
        return erro
    engine.dispose()
    return 'Agendamento atualizado com sucesso!'

# Delete
@router.delete('/{id}')
def deletar_agendamento(id : int):
    
    try:
        with engine.begin() as con:
            sql = """DELETE FROM agenda
                    WHERE id=:id;"""
            con.execute(text(sql), {"id": id})
            return 'Agendamento deletado com sucesso!'
    except Exception as e:
        return e
    
