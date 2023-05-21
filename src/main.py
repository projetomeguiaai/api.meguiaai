from fastapi import FastAPI
from . import routers
from .models import Base
from .database import engine
from fastapi import FastAPI


# Config do banco de dados
Base.metadata.create_all(bind=engine)

# Intancia FastAPI
app = FastAPI()
app.include_router(routers.tfmodels_router)

@app.get("/")
def main():
    return "Renan Alves"
