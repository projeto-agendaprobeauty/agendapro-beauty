import uvicorn
from fastapi import FastAPI
from routers.cliente import router as cliente_router
from routers.agenda import router as agenda_router

app = FastAPI()

app.include_router(cliente_router)
app.include_router(agenda_router)


@app.get('/')
def index():
    return {"Hello" : "World"}

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True)