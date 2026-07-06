from pydantic import BaseModel


class ProfissionalArea(BaseModel):
    area_id: int
    profissional_id: int