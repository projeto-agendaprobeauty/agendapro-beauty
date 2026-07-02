from pydantic import BaseModel, Field, EmailStr


class Agenda(BaseModel):
    status: str
    horario_inicial: str
    horario_final: str = 
    data: str = Field(min_length=10, max_length=10)
    cliente_id: int 
    profissional_id: int 
    servico_id: int 
    
