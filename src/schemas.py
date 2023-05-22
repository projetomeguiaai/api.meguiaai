from pydantic import BaseModel
from fastapi import UploadFile, File
from typing import Annotated


# Validação do model TFModel
class TFModel(BaseModel):
    id: int
    name: str
    model: str
    labels: list[str]

    class Config:
        orm_mode = True


# DTO para validação de uma criação de TFModel
class CreateTFModel(BaseModel):
    name: str
    model: str
    labels: list[str]

    class Config:
        orm_mode = True


# DTO para validação de uma adição de TFModel
class AddTFModel(BaseModel):
    name: str
    model_path: str
    labels: list[str]

    class Config:
        orm_mode = True


# DTO para validação de uma predict de TFModel
class ModelPredict(BaseModel):
    model_id: int
    img_path: str

    class Config:
        orm_mode = True
