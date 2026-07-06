import os
from fastapi import APIRouter
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
router = APIRouter(prefix='/cliente', tags=['Cliente'])

# Create

# Read (todos os clientes)
@router.get('')
def select_clientes():
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
    except Exception as e:
        return e
    engine.dispose()
    return result._mapping
# Update

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
    except Exception as e:
        return e
    