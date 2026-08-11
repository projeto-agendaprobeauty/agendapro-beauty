import os
from fastapi import APIRouter
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

print("Diretório atual:", os.getcwd())
print("DATABASE_URL:", os.getenv("DATABASE_URL"))


DATABASE_URL = os.getenv('DATABASE_URL')

router = APIRouter(prefix='/dashboard', tags=['dashboard'])

engine = create_engine(DATABASE_URL)

@router.get('')
def listar_dashboard():
    try:
        with engine.begin() as con:
            sql_total = """SELECT COUNT(*) AS total 
            FROM agenda"""

            resultado_total = con.execute(text(sql_total))
            total_agendamentos = resultado_total.fetchone()._mapping["total"]

            sql_servico = """SELECT s.nome, COUNT(*) AS total
                        FROM agenda a
                        JOIN servico s ON a.servico_id = s.id
                        GROUP BY s.nome
                        ORDER BY total DESC;"""
            resultado_servico = con.execute(text(sql_servico))
            servico = [dict(row._mapping) for row in resultado_servico]

            sql_profissionais = """SELECT u.nome, COUNT(*) AS total
                            FROM agenda a
                            JOIN profissional p ON a.profissional_id = p.id
                            JOIN usuario u ON p.usuario_id = u.id
                            GROUP BY u.nome
                            ORDER BY total DESC;"""
            resultado_profissional = con.execute(text(sql_profissionais))
            profissional = [dict(row._mapping) for row in resultado_profissional]

        return {
                "total_agendamentos": total_agendamentos,
                "servico_mais_solicitados": servico,
                "profissional_mais_requisitados": profissional
                
           } 
    
    except Exception as erro:
        print("ERRO:", erro)
        return {"erro": str(erro)}
        
            
