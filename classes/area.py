from pydantic import BaseModel, Field

class Area(BaseModel):
    nome: str = Field(min_length=4)