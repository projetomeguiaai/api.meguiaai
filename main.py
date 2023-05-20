from fastapi import FastAPI
from dotenv import load_dotenv

# Carrega a .env
load_dotenv()

# Cria a instância
app = FastAPI()


@app.get('/')
def asdf():
    return {"data": "data"}
