from pydantic import BaseModel, Field, EmailStr


class Agenda(BaseModel):
    status: str
    horario_inicial: str
    horario_final: str 
    data: int
    cliente_id: int 
    profissional_id: int 
    servico_id: int 
    
