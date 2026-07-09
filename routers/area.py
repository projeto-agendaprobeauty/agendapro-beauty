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


#READ
@router.get('')
def select_area():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """SELECT id, nome FROM public.area;"""
            response = con.execute(text(sql))
            result = response.mappings().all()
    except Exception as erro:
        return erro
    engine.dispose()
    return result

#READ (buscar area por id)
@router.get('/{id}')
def search_area(id : int):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """SELECT id, nome FROM public.area
                    WHERE id = :id;"""
            response = con.execute(text(sql), {"id": id})
            result = response.fetchone()
    except Exception as erro:
        return erro
    engine.dispose()
    return result._mapping
  
#UPDATE
@router.put('/{id}')
def update_area(id: int, area :Area):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con: 
            sql = """UPDATE public.area
                      SET nome= :nome
                      WHERE id= :id;"""          
            dados = {
                "id": id,
                "nome": area.nome,
            }
            con.execute(text(sql), dados)
    except Exception as erro:
        return "erro:"+erro
    engine.dispose()
    return 'Área atualizada com sucesso!'
  
#DELETE
@router.delete('/{id}')
def delete_area(id : int):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con:
            sql = """DELETE FROM public.area
                    WHERE id=:id;"""
            con.execute(text(sql), {"id": id})
            return 'Área deletada com sucesso!'
    except Exception as erro:
        return erro
      
