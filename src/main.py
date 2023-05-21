from fastapi import FastAPI
from . import routers
from .models import Base
from .database import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Config do banco de dados
Base.metadata.create_all(bind=engine)

# Intancia FastAPI
app = FastAPI()
app.include_router(routers.tfmodels_router)

# Habilta o CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Rota inicial
@app.get("/")
def main():
    file = open("./src/data/asdf.txt")
    return {"message": "Bem vindo a API Me Guia.AI!", "file": file}
