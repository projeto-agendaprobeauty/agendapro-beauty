from pydantic import BaseModel, Field, EmailStr
from datetime import date



class Agenda(BaseModel):
    status: str
    horario_inicial: str
    horario_final: str 
    data: date
    cliente_id: int 
    profissional_id: int 
    servico_id: int 
    
