import os
from fastapi import APIRouter
from dotenv import load_dotenv
from classes.usuario import Usuario
from sqlalchemy import create_engine, text

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
router = APIRouter(prefix='/usuario', tags=['Usuario'])

# Create
@router.post('')
def insert_usuario(usuario: Usuario):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """INSERT INTO public.usuario
                    (nome, senha, email, telefone, tipo_usuario)
                    VALUES (:nome, :senha, :email, :telefone, :tipo_usuario)"""

            dados = {
                "nome": usuario.nome,
                "senha": usuario.senha,
                "email": usuario.email,
                "telefone": usuario.telefone,
                "tipo_usuario": usuario.tipo_usuario
            }

            con.execute(text(sql), dados)

    except Exception as erro:
        return erro

    finally:
        engine.dispose()

    return "Usuário cadastrado com sucesso!"
  
#READ
@router.get('')
def select_usuario():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """SELECT id, nome, senha, email, telefone,tipo_usuario
                      FROM public.usuario;"""
            response = con.execute(text(sql))
            result = response.mappings().all()
    except Exception as e:
        return e
    engine.dispose()
    return result
  
#READ (busca usuario por id)
@router.get('/{id}')
def search_usuario(id : int):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """SELECT nome, email, telefone, tipo_usuario
                    FROM public.usuario 
                    WHERE id = :id;"""
            response = con.execute(text(sql), {"id": id})
            result = response.fetchone()
    except Exception as erro:
        return erro
    engine.dispose()
    return result._mapping
  
#UPDATE
@router.put('/{id}')
def update_usuario(id: int, usuario :Usuario):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con: 
            sql = """UPDATE public.usuario
                    SET nome= :nome,
                    senha= :senha, 
                    email= :email,
                    telefone = :telefone,
                    tipo_usuario = :tipo_usuario
                    WHERE id = :id;"""            
            dados = {
                "id": id, 
                "nome": usuario.nome,
                "senha": usuario.senha,
                "email": usuario.email,
                "telefone": usuario.telefone,
                "tipo_usuario": usuario.tipo_usuario
            }
            con.execute(text(sql), dados)
    except Exception as erro:
        return erro
    engine.dispose()
    return 'Usuário atualizado com sucesso!'
  
#DELETE
@router.delete('/{id}')
def delete_usuario(id : int):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con:
            sql = """DELETE FROM usuario
                    WHERE id=:id;"""
            con.execute(text(sql), {"id": id})

            return 'Usuário deletado com sucesso!'
    except Exception as erro:
        return erro