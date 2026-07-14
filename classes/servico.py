from pydantic import BaseModel, Field


class Servico(BaseModel):
    nome: str = Field(min_length=4)
    descricao: str = Field(min_length=10)
    duracao: int = Field(gt=0)
    preco: float = Field(gt=0)
    area_id: int