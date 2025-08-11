from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Amora Hub API funcionando"}
