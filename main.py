import os
import uvicorn
from fastapi import FastAPI

# 1. Importa o engine e a Base do seu arquivo banco_dados.py
from banco_dados import engine, Base  

# 2. Importa os modelos para o SQLAlchemy saber quais tabelas criar
import clientes


from controladores.controlador_clientes import router as clientes_router

app = FastAPI()

# 3. Esta linha cria todas as tabelas no banco de dados caso elas não existam
Base.metadata.create_all(bind=engine)

# 3. Esta linha força a exclusão das tabelas antigas e desatualizadas
#Base.metadata.drop_all(bind=engine)

# Esta linha cria todas as tabelas novas com as colunas corretas
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {
        "message": "Bem-vindo à Agenda Pro Beauty!",
        "status": "ok"
    }

app.include_router(clientes_router)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)