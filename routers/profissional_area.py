import os
from fastapi import APIRouter
from dotenv import load_dotenv
from sqlalchemy import create_engine, text


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
router = APIRouter(prefix='/profissional_area', tags=['ProfissionalArea'])
from classes.profissional_area import ProfissionalArea
##CD

#CREAT
@router.post('')
def insert_profissionalArea(profissionalarea :ProfissionalArea):
  engine = create_engine(DATABASE_URL)
  try:
        with engine.begin() as con:
            sql = """ INSERT INTO public.profissional_area(area_id, profissional_id)
                      VALUES(:area_id, :profissional_id);"""
            dados = {
              "area_id": profissionalarea.area_id,
              "profissional_id": profissionalarea.profissional_id
            }
            con.execute(text(sql),dados)
  except Exception as erro:
    return erro
  engine.dispose()
  return 'Associação cadastrado com sucesso!'

#DELETE
@router.delete('/{Profid}/{Areaid}')
def delete_profissionalArea(Profid: int, Areaid: int):
  engine = create_engine(DATABASE_URL)
  try:
        with engine.begin() as con:
            sql = """DELETE FROM public.profissional_area
                      WHERE area_id = :area_id AND profissional_id = :profissional_id;"""
            
            con.execute(text(sql), {
                "area_id": Areaid, 
                "profissional_id": Profid
            })
  except Exception as erro:
    return erro
  engine.dispose()
  return 'Associação deletada com sucesso!'