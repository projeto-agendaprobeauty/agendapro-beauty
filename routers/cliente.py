import os
from fastapi import APIRouter
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
router = APIRouter(prefix='/cliente', tags=['Cliente'])
from classes.cliente import Cliente

# Create
@router.post('')
def insert_cliente(cliente :Cliente):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con: 
            sql = """INSERT INTO public.cliente
                                (nome, email, telefone)
                        VALUES ( :nome, :email, :telefone)"""            
            dados = {
                "nome" : cliente.nome,
                "email": cliente.email,
                "telefone": cliente.telefone
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
            sql = """SELECT nome, email, telefone 
                    FROM cliente"""
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
            sql = """SELECT nome, email, telefone 
                    FROM cliente 
                    WHERE id = :id"""
            response = con.execute(text(sql), {"id": id})
            result = response.fetchone()
    except Exception as erro:
        return erro
    engine.dispose()
    return result._mapping
# Update
@router.put('/{id}')
def update_cliente(id: int, cliente :Cliente):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con: 
            sql = """UPDATE public.cliente
                    SET nome = :nome, 
                        email = :email, 
                        telefone = :telefone
                    WHERE id = :id"""            
            dados = {
                "id": id, 
                "nome": cliente.nome,
                "email": cliente.email,
                "telefone": cliente.telefone
            }
            con.execute(text(sql), dados)
    except Exception as erro:
        return erro
    engine.dispose()
    return 'Cliente atualizado com sucesso!'
# Delete
@router.delete('/{id}')
def delete_cliente(id : int):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con:
            sql = """DELETE FROM cliente
                    WHERE id=:id;"""
            con.execute(text(sql), {"id": id})
            return 'Cliente deletado com sucesso!'
    except Exception as erro:
        return erro
    