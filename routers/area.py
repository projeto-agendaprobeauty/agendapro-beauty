import os
from fastapi import APIRouter
from dotenv import load_dotenv
from sqlalchemy import create_engine, text


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
router = APIRouter(prefix='/area', tags=['Area'])
from classes.area import Area

#CREATE
@router.post('')
def insert_area(area :Area):
  engine = create_engine(DATABASE_URL)
  try:
        with engine.begin() as con:
            sql = """ INSERT INTO public.area (nome)
                    VALUES(:nome);"""
            dados = {
              "nome": area.nome,
            }
            con.execute(text(sql),dados)
  except Exception as erro:
    return erro
  engine.dispose()
  return 'Área cadastrada com sucesso!'
