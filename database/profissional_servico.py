from pydantic import BaseModel, Field, EmailStr


class ProfissionalServico(BaseModel):
    profissional_id: int
    servico_id: int