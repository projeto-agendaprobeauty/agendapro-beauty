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

            sql_servicos = """SELECT s.nome, COUNT(*) AS total
                        FROM agenda a
                        JOIN servicos s ON a.servico_id = s.id
                        GROUP BY s.nome
                        ORDER BY total DESC;"""
            resultado_servicos = con.execute(text(sql_servicos))
            servicos = [dict(row) for row in resultado_servicos]

            sql_profissionais = """SELECT p.nome, COUNT(*) AS total
                        FROM agenda a
                        JOIN profissionais p ON a.profissional_id = p.id
                        GROUP BY p.nome
                        ORDER BY total DESC;"""
            resultado_profissionais = con.execute(text(sql_profissionais))
            profissionais = [dict(row) for row in resultado_profissionais]

        return {
                "total_agendamentos": total_agendamentos,
                "servicos_mais_solicitados": servicos,
                "profissionais_mais_requisitados": profissionais
                
           } 

    except Exception as erro:
        print("ERRO:", erro)
        return {"erro": str(erro)}
        
    engine.dispose()