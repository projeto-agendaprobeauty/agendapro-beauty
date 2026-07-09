from pydantic import BaseModel, field_validator
from datetime import date, time

class Agenda(BaseModel):
    status: str
    horario_inicial: time
    horario_final: time
    data: date
    cliente_id: int 
    profissional_id: int 
    servico_id: int 

    @field_validator('status')
    def validaStatus(cls, value : str) -> str:
        if value == 'Marcado' or value == 'Cancelado' or value == 'Realizado':
            return value
        raise ValueError('Valor de status inválido')