# Casos de uso para os modelos treinados na API
from helpers.tensorflow import *
from typing import Annotated
from fastapi import UploadFile, File

def make_prediction(model_id, image):
    model = load_saved_model(model_id)

def get_all_models():
    pass

def create_model():
    pass
