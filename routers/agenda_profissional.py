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

@router.get("/{id}")
def get_agenda_profissional_by_id(id: int):
    with engine.begin() as connection:
        sql = """
            SELECT 
                ap.id AS agenda_profissional_id, 
                ap.data AS data_agenda,
                u.id AS usuario_id, 
                u.nome AS nome_profissional,
                COALESCE(
                    json_agg(
                        json_build_object(
                            'agenda_id', a.id,
                            'horario_inicio', a.horario_inicio::text,
                            'horario_fim', a.horario_fim::text,
                            'status', a.status,
                            'servico_id', a.servico_id,
                            'cliente_id', a.cliente_id
                        )
                    ) FILTER (WHERE a.id IS NOT NULL), '[]'
                ) AS horarios_agendados
            FROM public.agenda_profissional ap
            JOIN public.profissional p ON ap.profissional_id = p.id
            JOIN public.usuario u ON p.usuario_id = u.id
            LEFT JOIN public.agenda a ON a.profissional_id = ap.profissional_id 
                                      AND a.data = ap.data
            WHERE ap.id = :id
            GROUP BY ap.id, ap.data, u.id, u.nome
        """
        result = connection.execute(text(sql), {"id": id})
        agenda_profissional = result.fetchone()
        
        if not agenda_profissional:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Agenda do profissional não encontrada"
            )
            
        return dict(agenda_profissional._mapping)

@router.put("/{id}")
def update_agenda_profissional(id: int, agenda_profissional: Agenda_Profissional):  
    try:
        with engine.begin() as connection:
            sql = """UPDATE agenda_profissional 
                     SET profissional_id = :profissional_id, data = :data 
                     WHERE id = :id"""
            dados = {
                "profissional_id": agenda_profissional.profissional_id,
                "data": agenda_profissional.data,
                "id": id
            }
            result = connection.execute(text(sql), dados)
            
            if result.rowcount == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agenda do profissional não encontrada")
            
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    return {"message": "Agenda do profissional atualizada com sucesso!"}

@router.delete("/{id}")
def delete_agenda_profissional(id: int):    
    try:
        with engine.begin() as connection:
            sql = "DELETE FROM agenda_profissional WHERE id = :id"
            result = connection.execute(text(sql), {"id": id})
            
            if result.rowcount == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agenda do profissional não encontrada")
            
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    return {"message": "Agenda do profissional deletada com sucesso!"}  

