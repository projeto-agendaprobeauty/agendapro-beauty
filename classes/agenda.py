from datetime import date
from pydantic import BaseModel

class Agenda(BaseModel):
    status: str
    horario_inicial: str
    horario_final: str
    data: date
    cliente_id: int
    profissional_id: int
    servico_id: int
