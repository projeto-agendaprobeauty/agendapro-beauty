from sqlalchemy import Column, Integer, String
from banco_dados import Base

class Agenda(Base):
    __tablename__ = "agenda"

    id = Column(Integer, primary_key=True, index=True)
    data_hora_inicia = Column(String(20), nullable=False)
    data_hora_termina = Column(String(20), nullable=False)
    id_cliente = Column(Integer, nullable=False)
    id_profissional = Column(Integer, nullable=False)
    id_servico = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False)
