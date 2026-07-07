from pydantic import BaseModel, Field


class Servico(BaseModel):
    nome_servico: str = Field(min_length=2)
    descricao: str = Field(min_length=2)
    duracao: int
    valor: float = Field(gt=0)
    