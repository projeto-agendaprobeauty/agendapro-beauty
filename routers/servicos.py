import os
from fastapi import APIRouter
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
router = APIRouter(prefix='/servicos', tags=['Servicos'])

from classes.servico import Servico

#CREATE
@router.post('')
def cadastrar_servicos(servicos :Servicos):
  engine = create_engine(DATABASE_URL)
  try:
        with engine.begin() as con:
            sql = """ INSERT INTO public.servico (nome, preco, duracao, id_area)
                    VALUES(:nome, :preco, :duracao, :id_area);"""
            dados = {
              "nome": servicos.nome,
              "preco": servicos.preco,
              "duracao": servicos.duracao,
              "id_area": servicos.id_area
            }
            con.execute(text(sql),dados)
  except Exception as erro:
    return erro
  engine.dispose()
  return 'Serviço cadastrado com sucesso!'

@router.get('')
def consultar_servico():   
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """SELECT id, nome, preco, duracao, id_area FROM public.servico;"""
            response = con.execute(text(sql))
            result = response.mappings().all()
    except Exception as erro:
        return erro
    engine.dispose()
    return result

@router.get('/{id}')
def consultar_servico_por_id(id : int):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """SELECT id, nome, preco, duracao, id_area FROM public.servico
                    WHERE id = :id;"""
            response = con.execute(text(sql), {"id": id})
            result = response.fetchone()
    except Exception as erro:
        return erro
    engine.dispose()
    return result._mapping

@router.put('/{id}')
def atualizar_servicos(id : int, servicos : Servicos):    
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con:
            sql = """UPDATE public.servico
                    SET nome = :nome, preco = :preco, duracao = :duracao, id_area = :id_area
                    WHERE id = :id;"""
            dados = {
              "id": id,
              "nome": servicos.nome,
              "preco": servicos.preco,
              "duracao": servicos.duracao,
              "id_area": servicos.id_area
            }
            con.execute(text(sql),dados)
    except Exception as erro:
        return erro
    engine.dispose()
    return 'Serviço atualizado com sucesso!'

