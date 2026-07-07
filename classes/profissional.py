from pydantic import BaseModel, Field, EmailStr


class Profissional(BaseModel):
    nome: str = Field(min_length=2)
    email: EmailStr
    horario_inicio: str 
    horario_fim: str 