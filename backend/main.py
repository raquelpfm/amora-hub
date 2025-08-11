# main.py
from fastapi import FastAPI
from app.db.session import engine
from app.models.base import Base

app = FastAPI(
    title="Amora Hub API",
    description="API para o gerenciamento colaborativo de atividades domésticas.",
    version="0.1.0"
)

@app.on_event("startup")
async def on_startup():
    # Cria as tabelas no banco de dados
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def read_root():
    return {"Project": "Bem-vindo(a) ao Amora Hub!"}