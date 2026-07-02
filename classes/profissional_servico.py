from pydantic import BaseModel, Field


class ProfissionalServico(BaseModel):
    profissional_id: int
    servico_id: int