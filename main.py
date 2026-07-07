import uvicorn
from fastapi import FastAPI
from routers.cliente import router as cliente_router
from routers.profissional import router as profissional_router
from routers.area import router as area_router

app = FastAPI()
app.include_router(cliente_router)
app.include_router(profissional_router)
app.include_router(area_router)
@app.get('/')
def index():
    return {"Hello" : "World"}

if __name__ == '__main__':
    uvicorn.run("main:app",
                #host='0.0.0.0',
                port=80,
                reload=True)