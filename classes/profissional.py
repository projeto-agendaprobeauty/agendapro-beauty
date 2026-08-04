from pydantic import BaseModel, Field, EmailStr
from datetime import time


class Profissional(BaseModel):
    usuario_id: str
    horario_inicio: time
    horario_fim: time