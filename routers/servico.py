import os
from fastapi import APIRouter
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
router = APIRouter(prefix='/servico', tags=['Servico'])
from classes.servico import Servico

#CREATE
@router.post('')
def insert_servico(servico :Servico):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con:
            sql = """INSERT INTO public.servico(nome, descricao, duracao, preco, area_id)
                    VALUES(:nome, :descricao, :duracao, :preco, :area_id);"""
            dados = {
            "nome": servico.nome,
            "descricao":servico.descricao,
            "duracao": servico.duracao,
            "preco": servico.preco,
            "area_id": servico.area_id
            }
            con.execute(text(sql),dados)
    except Exception as erro:
        return erro
    engine.dispose()
    return 'Serviço cadastrado com sucesso!'
  
#READ
@router.get('')
def select_servico():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """SELECT id, nome, descricao, duracao, preco, area_id
                      FROM public.servico;"""
            response = con.execute(text(sql))
            result = response.mappings().all()
    except Exception as erro:
        return erro
    engine.dispose()
    return result
  
#READ (buscar servico por id)
@router.get('/{id}')
def search_servico(id : int):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """SELECT id, nome, descricao, duracao, preco, area_id
                      FROM public.servico
                    WHERE id = :id"""
            response = con.execute(text(sql), {"id": id})
            result = response.fetchone()
    except Exception as erro:
        return erro
    engine.dispose()
    return result._mapping

#UPDATE
@router.put('/{id}')
def update_servico(id: int, servico :Servico):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con: 
            sql = """UPDATE public.servico
                      SET nome= :nome, 
                      descricao= :descricao, 
                      duracao= :duracao, 
                      preco= :preco, 
                      area_id= :area_id
                    WHERE id = :id"""     
            dados = {
                "id": id,
                "nome": servico.nome,
                "descricao":servico.descricao,
                "duracao": servico.duracao,
                "preco": servico.preco,
                "area_id": servico.area_id
            }
            con.execute(text(sql), dados)
    except Exception as erro:
        return "erro:"+erro
    engine.dispose()
    return 'Serviço atualizado com sucesso!'

#DELETE
@router.delete('/{id}')
def delete_servico(id : int):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con:
            sql = """ DELETE FROM public.servico
                    WHERE id=:id;"""
            con.execute(text(sql), {"id": id})
            return 'Serviço deletado com sucesso!'
    except Exception as erro:
        return erro