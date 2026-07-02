from sqlalchemy import Column, Integer, String
from banco_dados import Base

class Profissional(Base):
    __tablename__ = "profissionais"

    id = Column(Integer, primary_key=True, index=True)
    nome_profissional = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=False)
    email = Column(String(150), unique=True, nullable=False)  

