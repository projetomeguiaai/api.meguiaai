from sqlalchemy.orm import Session
from . import models
from .helpers.tensorflow_helper import *
from .schemas import *
from fastapi import File, UploadFile
from typing import Annotated
import base64
import io
import h5py

# Seleciona todos os tfmodels do banco
def find_all_tfmodels(db: Session, skip: int = 0, limit: int = 100):
  return (
    db.query(models.TFModel)
    .offset(skip)
    .limit(limit)
    .all()
  )

# Seleciona um model pelo id
def find_tfmodel_by_id(db: Session, id: int):
  return (
    db.query(models.TFModel)
    .filter_by(id=id)
    .first()
  )

# Adiciona um model como base64
def add_tfmodel(db: Session, model: AddTFModel):
  name = model.name
  tfmodel = open(model.model_path, "rb")
  labels = model.labels

  modelb64 = base64.b64encode(tfmodel.read())

  new_model = models.TFModel(
    name=name,
    model=modelb64,
    labels=labels
  )

  db.add(new_model)
  db.commit()
  db.refresh(new_model)

  return new_model


def predict_img(pred: ModelPredict, db: Session):
  model = db.query(models.TFModel).filter_by(id=pred.model_id).first()

  model_bin = base64.b64decode(model.model)

  tfmodel_path = f"./src/data/{model.name}.h5"

  with open(tfmodel_path, "wb") as f:
    f.write(model_bin)
  
  prediction = predict(model=tfmodel_path, img_path=pred.img_path, labels=model.labels)

  os.remove(tfmodel_path)

  return prediction
