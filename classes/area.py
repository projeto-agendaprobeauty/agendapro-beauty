from pydantic import BaseModel, Field

class Area(BaseModel):
    nome_area: str = Field(min_length=4)