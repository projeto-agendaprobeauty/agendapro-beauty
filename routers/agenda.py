import os
from fastapi import APIRouter, HTTPException, status
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from classes.agenda import Agenda

load_dotenv()

print("Diretório atual:", os.getcwd())
print("DATABASE_URL:", os.getenv("DATABASE_URL"))

DATABASE_URL = os.getenv('DATABASE_URL')

router = APIRouter(prefix='/agenda', tags=['Agenda'])
engine = create_engine(DATABASE_URL)


# Create (Cadastrar Agendamento)
@router.post('', status_code=status.HTTP_201_CREATED)
def cadastrar_agendamento(agenda: Agenda):
    try:
        with engine.begin() as con:
            sql = """INSERT INTO public.agenda
                    (status, horario_inicio, horario_fim, data, cliente_id, profissional_id, servico_id)
                VALUES (:status, :horario_inicio, :horario_fim, :data, :cliente_id, :profissional_id, :servico_id)"""
            
            dados = {
                "status": agenda.status,
                "horario_inicio": agenda.horario_inicio,
                "horario_fim": agenda.horario_fim,
                "data": agenda.data,
                "cliente_id": agenda.cliente_id,
                "profissional_id": agenda.profissional_id,
                "servico_id": agenda.servico_id
            }

            resultado = con.execute(text(sql), dados)
            print("Linhas afetadas:", resultado.rowcount)
            return {"mensagem": "Agendamento cadastrado com sucesso!"}
            
    except Exception as erro:
        print("ERRO:", erro)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Erro ao cadastrar agendamento: {str(erro)}"
        )


# Escolher Serviços
@router.get("/opcoes_servico")
def listar_servicos():
    try:
        with engine.connect() as con:
            sql = """SELECT 
                p.id AS profissional_id,
                u.nome AS profissional_nome,
                s.id AS servico_id,
                s.nome AS servico_nome
            FROM profissional_servico ps
            JOIN profissional p ON ps.profissional_id = p.id
            JOIN usuario u ON p.usuario_id = u.id
            JOIN servico s ON ps.servico_id = s.id;"""

            response = con.execute(text(sql))
            return response.mappings().all()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Erro ao buscar opções de serviços: {str(e)}"
        )


# Read (Todos os agendamentos)
@router.get('')
def listar_agendamentos():
    try:
        with engine.connect() as con:
            sql = sql = """SELECT 
                    a.id, 
                    a.cliente_id, 
                    usuario.nome AS cliente_nome, 
                    a.servico_id, 
                    servico.nome AS servico_nome, 
                    a.profissional_id, 
                    usuario_prof.nome AS profissional_nome,
                    a.data, 
                    a.horario_inicio, 
                    a.horario_fim, 
                    a.status
            FROM agenda a 
            JOIN cliente ON a.cliente_id = cliente.id
            JOIN usuario ON cliente.usuario_id = usuario.id
            JOIN profissional ON a.profissional_id = profissional.id
            JOIN usuario usuario_prof ON profissional.usuario_id = usuario_prof.id
            JOIN servico ON a.servico_id = servico.id
            ORDER BY a.data ASC;"""
            
            response = con.execute(text(sql))
            result = []
            for row in response:
                linha = row._mapping
                agenda = {
                    linha['id']: {
                        "cliente": {
                            "id": linha['cliente_id'],
                            "nome": linha['cliente_nome']
                        },
                        "servico": {
                            "id": linha['servico_id'],
                            "nome": linha['servico_nome']
                        },
                        "profissional": {
                            "id": linha['profissional_id'],
                            "nome": linha['profissional_nome']
                        },
                        "inicio": str(linha['horario_inicio']),
                        "fim": str(linha['horario_fim']),
                        "status": linha['status']
                    }
                }
                result.append(agenda)
            return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Erro ao listar agendamentos: {str(e)}"
        )


# Read (Buscar agendamento por ID)
@router.get('/{id}')
def buscar_agendamento(id: int):
    try:
        with engine.connect() as con:
            sql = """SELECT a.id, a.cliente_id, cliente.nome as cliente_nome, 
                            a.servico_id, servico.nome as servico_nome, 
                            a.profissional_id, profissional.nome as profissional_nome, 
                            data, a.horario_inicio, a.horario_fim, status
                    FROM agenda a 
                    JOIN cliente ON a.cliente_id = cliente.id 
                    JOIN profissional ON a.profissional_id = profissional.id
                    JOIN servico ON a.servico_id = servico.id
                    WHERE a.id = :id
                    ORDER BY data ASC;"""
            
            response = con.execute(text(sql), {"id": id})
            row = response.fetchone()
            
            if not row:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, 
                    detail="Agendamento não encontrado."
                )

            linha = row._mapping
            return {
                "cliente": {
                    "id": linha['cliente_id'],
                    "nome": linha['cliente_nome']
                },
                "servico": {
                    "id": linha['servico_id'],
                    "nome": linha['servico_nome']
                },
                "profissional": {
                    "id": linha['profissional_id'],
                    "nome": linha['profissional_nome']
                },
                "inicio": str(linha['horario_inicio']),
                "fim": str(linha['horario_fim']),
                "status": linha['status']
            }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Erro ao buscar agendamento: {str(e)}"
        )


# Update (Atualizar Agendamento)
@router.put('/{id}')
def atualizar_agendamento(id: int, agenda: Agenda):
    try:
        with engine.begin() as con:
            sql = """UPDATE public.agenda
                    SET status = :status,
                        horario_inicio = :horario_inicio,
                        horario_fim = :horario_fim,
                        data = :data,
                        cliente_id = :cliente_id,
                        profissional_id = :profissional_id,
                        servico_id = :servico_id
                    WHERE id = :id"""
            
            dados = {
                "id": id,
                "status": agenda.status,
                "horario_inicio": agenda.horario_inicio,
                "horario_fim": agenda.horario_fim,
                "data": agenda.data,
                "cliente_id": agenda.cliente_id,
                "profissional_id": agenda.profissional_id,
                "servico_id": agenda.servico_id
            }
            resultado = con.execute(text(sql), dados)
            
            if resultado.rowcount == 0:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, 
                    detail="Agendamento não encontrado para atualização."
                )
                
            return {"mensagem": "Agendamento atualizado com sucesso!"}
    except HTTPException:
        raise
    except Exception as erro:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Erro ao atualizar agendamento: {str(erro)}"
        )


# Delete (Deletar Agendamento)
@router.delete('/{id}')
def deletar_agendamento(id: int):
    try:
        with engine.begin() as con:
            sql = "DELETE FROM agenda WHERE id = :id;"
            resultado = con.execute(text(sql), {"id": id})
            
            if resultado.rowcount == 0:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, 
                    detail="Agendamento não encontrado para exclusão."
                )
                
            return {"mensagem": "Agendamento deletado com sucesso!"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Erro ao deletar agendamento: {str(e)}"
        )

    
