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
             
            sql = """INSERT INTO public.agenda
                    (status, horario_inicial, horario_fim, data, cliente_id, profissional_id, servico_id)
                VALUES ( :status, :horario_inicial, :horario_fim, :data, :cliente_id, :profissional_id, :servico_id)"""            
            dados = {
                "status": agenda.status,
                "horario_inicial": agenda.horario_inicial,
                "horario_fim": agenda.horario_fim,
                "data": agenda.data,
                "cliente_id": agenda.cliente_id,
                "profissional_id": agenda.profissional_id,
                "servico_id": agenda.servico_id
            }

            resultado = con.execute(text(sql), dados)
            print("Linhas afetadas:", resultado.rowcount)

    except Exception as erro:
        return erro
    engine.dispose()
    return 'Agendamento cadastrado com sucesso!'

# Read (todos os agendamentos)
@router.get('')
def listar_agendamentos():
    
    try:
        with engine.connect() as con:
            sql = """SELECT status, horario_inicial, horario_fim, data, cliente_id, profissional_id, servico_id 
                    FROM agenda"""
            response = con.execute(text(sql))
            result = response.mappings().all()
    except Exception as e:
        return e
    engine.dispose()
    return result

# Read (buscar agendamento por id)
@router.get('/{id}')
def buscar_agendamento(id : int):

    
    try:
        with engine.connect() as con:
            sql = """SELECT status, horario_inicial, horario_fim, data, cliente_id, profissional_id, servico_id
                    FROM agenda
                    WHERE id = :id"""
            response = con.execute(text(sql), {"id": id})
            result = response.fetchone()
    except Exception as e:
        return e
    engine.dispose()
    return result._mapping
    
@router.put('/{id}')
def atualizar_agendamento(id: int, agenda :Agenda):
    
    try:
        with engine.begin() as con: 
            sql = """UPDATE public.agenda
                    SET status = :status,
                        horario_inicial = :horario_inicial,
                        horario_fim = :horario_fim,
                        data = :data,
                        cliente_id = :cliente_id,
                        profissional_id = :profissional_id,
                        servico_id = :servico_id
                    WHERE id = :id"""
            dados = {
                "id": id,
                "status": agenda.status,
                "horario_inicial": agenda.horario_inicial,
                "horario_fim": agenda.horario_fim,
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
    
