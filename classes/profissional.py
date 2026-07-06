from pydantic import BaseModel, Field, EmailStr


class Profissional(BaseModel):
    nome_profissional: str = Field(min_length=2)
    email: EmailStr
    horario_inicial: str 
    horario_final: str 