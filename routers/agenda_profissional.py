import os
from fastapi import APIRouter, HTTPException, status
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from classes.agenda_profissional import Agenda_Profissional

load_dotenv()

print("Diretório atual:", os.getcwd())
print("DATABASE_URL:", os.getenv("DATABASE_URL"))

DATABASE_URL = os.getenv('DATABASE_URL')

router = APIRouter(prefix='/agenda_profissional', tags=['Agenda_Profissional'])

engine = create_engine(DATABASE_URL)

@router.get("")
def get_agenda_profissional():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM agenda_profissional"))
        agenda_profissional_list = [dict(row._mapping) for row in result]
    
    return agenda_profissional_list

@router.post("")
def create_agenda_profissional(agenda_profissional: Agenda_Profissional):
    
    try:
       with engine.begin() as connection:

        sql = """INSERT INTO agenda_profissional (profissional_id, data) 
              VALUES (:profissional_id, :data)"""

        dados = {
            "profissional_id": agenda_profissional.profissional_id,
                "data": agenda_profissional.data
        }
            
        connection.execute(text(sql), dados)
            
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    return {"message": "Agenda do profissional criada com sucesso!"}

