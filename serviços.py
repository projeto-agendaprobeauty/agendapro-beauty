from sqlalchemy import Column, Integer, String
from banco_dados import Base

class Servico(Base):
    __tablename__ = "servicos"

    id = Column(Integer, primary_key=True, index=True)
    nome_servico = Column(String(100), nullable=False)
    descricao = Column(String(200), nullable=False)
    valor = Column(String(20), nullable=False)
     

