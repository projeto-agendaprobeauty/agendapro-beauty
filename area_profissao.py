from sqlalchemy import Column, Integer, String
from banco_dados import Base

class AreaProfissao(Base):
    
   
    nome_area: std  = Column(String(100), nullable=False)
    
     

