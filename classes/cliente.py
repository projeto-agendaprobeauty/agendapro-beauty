from pydantic import BaseModel, Field, EmailStr

# Schema de Cliente
class Cliente(BaseModel):
    nome: str = Field(min_length=2)
    email: EmailStr
    telefone: str
