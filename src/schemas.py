from pydantic import BaseModel
from fastapi import UploadFile, File
from typing import Annotated


# Schemas para validação dos dados
class TFModel(BaseModel):
    id: int
    name: str
    model: str
    labels: list[str]

    class Config:
        orm_mode = True


class CreateTFModel(BaseModel):
    name: str
    model: str
    labels: list[str]

    class Config:
        orm_mode = True


class AddTFModel(BaseModel):
    name: str
    model_path: str
    labels: list[str]

    class Config:
        orm_mode = True


class ModelPredict(BaseModel):
    model_id: int
    img_path: str

    class Config:
        orm_mode = True
