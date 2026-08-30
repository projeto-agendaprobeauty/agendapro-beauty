import os
from fastapi import APIRouter
from dotenv import load_dotenv
from classes.cliente import Cliente
from sqlalchemy import create_engine, text

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
router = APIRouter(prefix='/cliente', tags=['Cliente'])

# Create
@router.post('')
def insert_cliente(cliente :Cliente):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con: 
            sql = """INSERT INTO public.cliente
                                (usuario_id)
                        VALUES ( :usuario_id)"""            
            dados = {
                "usuario_id": cliente.usuario_id
            }
            con.execute(text(sql), dados)
    except Exception as erro:
        return erro
    engine.dispose()
    return 'Cliente cadastrado com sucesso!'
# Read (todos os clientes)
@router.get('')
def select_cliente():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """SELECT usuario.nome, usuario.email, usuario.telefone 
                    FROM cliente
                    JOIN usuario 
                    ON cliente.usuario_id = usuario.id"""
            response = con.execute(text(sql))
            result = response.mappings().all()
    except Exception as e:
        return e
    engine.dispose()
    return result

# Read (buscar cliente por id)
@router.get('/{id}')
def search_cliente(id : int):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """SELECT usuario.nome, usuario.email, usuario.telefone 
                    FROM cliente
                    JOIN usuario 
                    ON cliente.usuario_id = usuario.id 
                    WHERE cliente.id = :id"""
            response = con.execute(text(sql), {"id": id})
            result = response.fetchone()
    except Exception as erro:
        return erro
    engine.dispose()
    return result._mapping
