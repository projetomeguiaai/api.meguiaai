from .import schemas
from .database import get_db
from . import usecases
from fastapi import Depends, APIRouter, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated


# Router para os TFModels
tfmodels_router = APIRouter(
  prefix="/v1/models",
  tags=["models"]
)

# Rota inicial
@tfmodels_router.get("/", response_model=list[schemas.TFModel])
def tfmodel_all(db: Session = Depends(get_db)):
  return usecases.find_all_tfmodels(db)


# pega um model pelo id
@tfmodels_router.get("/{id}", response_model=schemas.TFModel)
def tfmodel_by_id(id: int, db: Session = Depends(get_db)):
  db_model = usecases.find_tfmodel_by_id(id=id, db=db)
  if db_model is None:
      raise HTTPException(status_code=404, detail="model not found")

  return db_model


# Adiciona um model ja existente
@tfmodels_router.post("/add")
def tfmodel_add(model: schemas.AddTFModel, db: Session = Depends(get_db)):
  return usecases.add_tfmodel(db=db, model=model)


# Faz uma predicao com o model do id
@tfmodels_router.post("/predict")
def tfmodel_predict(pred: schemas.ModelPredict, db: Session = Depends(get_db)):
  db_model = usecases.find_tfmodel_by_id(id=pred.model_id, db=db)
  if db_model is None:
      raise HTTPException(status_code=404, detail="model not found")
  return usecases.predict_img(pred, db=db)
  
