import uvicorn
from fastapi import FastAPI
from helpers.tensorflow.tensorflow_helper import run_model

app = FastAPI()

@app.get("/")
def root():
    return {"data": "Teste"}
