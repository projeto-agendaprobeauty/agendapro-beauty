from pydantic import BaseModel, Field, EmailStr
from datetime import time


class Profissional(BaseModel):
    nome_profissional: str = Field(min_length=3)
    email: EmailStr
    horario_inicial: time
    horario_final: time