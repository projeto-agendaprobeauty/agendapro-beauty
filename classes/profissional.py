from pydantic import BaseModel, Field, EmailStr
from datetime import time


class Profissional(BaseModel):
    nome: str = Field(min_length=3)
    email: EmailStr
    horario_inicio: time
    horario_fim: time