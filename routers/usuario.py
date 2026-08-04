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
def insert_usuario(usuario :Usuario):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con: 
            sql = """INSERT INTO public.usuario
                    (nome, senha, email, telefone)
                    VALUES(:nome, :senha, :email, :telefone);"""            
            dados = {
                "nome" : usuario.nome,
                "senha": usuario.senha,
                "email": usuario.email,
                "telefone": usuario.telefone
            }
            con.execute(text(sql), dados)
    except Exception as erro:
        return erro
    engine.dispose()
    return 'Usuário cadastrado com sucesso!'