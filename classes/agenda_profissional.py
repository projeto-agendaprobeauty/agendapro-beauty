from pydantic import BaseModel, Field, model_validator, field_serializer
from datetime import date, time

class Agenda_Profissional(BaseModel):
    
    profissional_id: int = Field(..., gt=0, description="O ID deve ser maior que 0")
    data: date = Field(..., description="A data deve estar no formato YYYY-MM-DD")


    @field_serializer('data')
    def formatar_data(self, data: date):
        return data.strftime('%d/%m/%Y')