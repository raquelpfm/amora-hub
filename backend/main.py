# cria aplicação FastAPI
# define uma única rota (endpoint) na raiz (/)

from fastapi import FastAPI

# Cria a instância principal da aplicação FastAPI
app = FastAPI(
    title="Amora Hub API",
    description="API para o gerenciamento colaborativo de atividades domésticas.",
    version="0.1.0"
)

@app.get("/")
def read_root():
    """
    Endpoint raiz que retorna uma mensagem de boas-vindas.
    """
    return {"Project": "Bem-vindo(a) ao Amora Hub!"}