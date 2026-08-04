from pydantic import BaseModel, Field, EmailStr, field_validator

class Usuario(BaseModel):
  nome: str = Field(min_length=3)
  senha: str = Field(min_length=6, max_length= 16)
  email: EmailStr
  telefone: str = Field(min_length=11, max_length=11)
  
  @field_validator('nome')
  def nomeEspaco(cls, value: str) -> str:
    if value.count(' ') == 0:
      raise ValueError('O nome deve conter pelo menos um sobrenome')
    return value.title()
  @field_validator('telefone')
  def validaTelefone(cls, value : str) -> str:
    if not value.isdigit():
      raise ValueError('O telefone de contato deve conter apenas números')
    return value
  
