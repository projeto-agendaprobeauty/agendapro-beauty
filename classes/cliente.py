from pydantic import BaseModel, Field, EmailStr, field_validator

# Schema de Cliente
class Cliente(BaseModel):
    usuario_id: int