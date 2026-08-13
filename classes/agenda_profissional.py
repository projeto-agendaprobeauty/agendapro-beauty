from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import date, time,field_serializer

class AgendaProfissional(BaseModel):
    id: int = Field(..., gt=0, description="O ID deve ser maior que 0")
    profissional_id: int = Field(..., gt=0, description="O ID deve ser maior que 0")
    data: str = Field(..., description="A data deve estar no formato YYYY-MM-DD")


@field_serializer('data')
    def formatar_data(self, data: date):
        return data.strftime('%d/%m/%Y')