import os
from fastapi import APIRouter
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
router = APIRouter(prefix='/profissional_servico', tags=['ProfissionalServico'])
from classes.profissional_servico import ProfissionalServico

#CREAT
@router.post('')
def insert_profissionalServico(profissionalservico :ProfissionalServico):
  engine = create_engine(DATABASE_URL)
  try:
        with engine.begin() as con:
            sql = """ INSERT INTO public.profissional_servico(profissional_id, servico_id)
                        VALUES(:profissional_id, :servico_id);"""
            dados = {
              "profissional_id": profissionalservico.profissional_id,
              "servico_id": profissionalservico.servico_id
            }
            con.execute(text(sql),dados)
  except Exception as erro:
    return erro
  engine.dispose()
  return 'Associação cadastrado com sucesso!'

#DELETE
@router.delete('/{Profid}/{Servid}')
def delete_profissionalArea(Profid: int, Servid: int):
  engine = create_engine(DATABASE_URL)
  try:
        with engine.begin() as con:
            sql = """DELETE FROM public.profissional_servico
                      WHERE servico_id = :servico_id AND profissional_id = :profissional_id;"""
            
            con.execute(text(sql), {
                "servico_id": Servid, 
                "profissional_id": Profid
            })
  except Exception as erro:
    return erro
  engine.dispose()
  return 'Associação deletada com sucesso!'