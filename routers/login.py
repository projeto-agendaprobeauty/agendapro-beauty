import os
from fastapi import APIRouter
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from pydantic import EmailStr

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
router = APIRouter(prefix='/login', tags=['Login'])

@router.get('/{usuarioEmail}')
def usuario_existe(usuarioEmail : EmailStr):
  engine = create_engine(DATABASE_URL)
  try:
    with engine.connect() as con:
      sql = """ SELECT 1 FROM usuario WHERE email = :usuarioEmail; """
      response = con.execute(text(sql), {"usuarioEmail": usuarioEmail})
      result = response.fetchone()
      if result is None:
        result = 'Usuário não cadastrado.'
      else:
        result = 'Usuário cadastrado.'
  except Exception as erro:
    return erro
  engine.dispose()
  return result