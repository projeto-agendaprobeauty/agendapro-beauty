from datetime import date, time
from pydantic import BaseModel, field_validator

class Agenda(BaseModel):
    status: str
    horario_inicial: time
    data: date
    cliente_id: int 
    profissional_id: int 
    servico_id: int 

    @field_validator('status')
    def validaStatus(cls, value : str) -> str:
        if value == 'Marcado' or value == 'Cancelado' or value == 'Realizado':
            return value
        raise ValueError('Valor de status inválido')

    @field_validator('horario_inicial')
    def formataHorario(cls, value : time) -> time:
        return value.strftime("%H:%M")
