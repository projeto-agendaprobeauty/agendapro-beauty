from sqlalchemy import Column, Integer, String
from banco_dados import Base

class AreaProfissao(Base):
    __tablename__ = "area_profissao"

    id = Column(Integer, primary_key=True, index=True)
    nome_area = Column(String(100), nullable=False)
    
     

