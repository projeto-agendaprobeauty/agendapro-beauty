import os
from fastapi import APIRouter
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
router = APIRouter(prefix='/profissional', tags=['Profissional'])
from classes.profissional import Profissional

#CREATE
@router.post('')
def insert_profissional(profissional :Profissional):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con:
            sql = """INSERT INTO public.profissional
                    (nome, email, horario_inicio, horario_fim)
                    VALUES(:nome, :email, :horario_inicio, :horario_fim);"""
            dados = {
            "nome": profissional.nome,
            "email":profissional.email,
            "horario_inicio": profissional.horario_inicio,
            "horario_fim": profissional.horario_fim
            }
            con.execute(text(sql),dados)
    except Exception as erro:
        return erro
    engine.dispose()
    return 'Profissional cadastrado com sucesso!'

#READ
@router.get('')
def select_profissional():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """SELECT id, nome, email, horario_inicio, horario_fim
                    FROM public.profissional;"""
            response = con.execute(text(sql))
            result = response.mappings().all()
    except Exception as erro:
        return erro
    engine.dispose()
    return result

#READ (buscar profissonal por id)
@router.get('/{id}')
def search_profissional(id : int):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """SELECT nome, email, horario_inicio, horario_fim 
                    FROM public.profissional 
                    WHERE id = :id"""
            response = con.execute(text(sql), {"id": id})
            result = response.fetchone()
    except Exception as erro:
        return erro
    engine.dispose()
    return result._mapping

#UPDATE
@router.put('/{id}')
def update_profissional(id: int, profissional :Profissional):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con: 
            sql = """UPDATE public.profissional
                    SET nome = :nome, 
                        email = :email, 
                        horario_inicio = :horario_inicio,
                        horario_fim = :horario_fim
                    WHERE id = :id"""     
            dados = {
                "id": id,
                "nome": profissional.nome,
                "email":profissional.email,
                "horario_inicio": profissional.horario_inicio,
                "horario_fim": profissional.horario_fim
            }
            con.execute(text(sql), dados)
    except Exception as erro:
        return "erro:"+erro
    engine.dispose()
    return 'Profissional atualizado com sucesso!'

#DELETE
@router.delete('/{id}')
def delete_profissional(id : int):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con:
            sql = """DELETE FROM public.profissional
                    WHERE id=:id;"""
            con.execute(text(sql), {"id": id})
            return 'Profissional deletado com sucesso!'
    except Exception as erro:
        return erro
    