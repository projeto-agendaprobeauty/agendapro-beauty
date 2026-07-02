from pydantic import BaseModel, Field, EmailStr

# Schema de Cliente
class Cliente(BaseModel):
    nome_cliente: str = Field(min_length=2)
    email: str
    cidade: str
