from sqlalchemy.orm import Session
from . import models
from .helpers.tensorflow_helper import *
from .schemas import TFModel

# Seleciona todos os tfmodels do banco
def find_all_tfmodels(db: Session, skip: int = 0, limit: int = 100):
  return (
    db.query(models.TFModel)
    .offset(skip)
    .limit(limit)
    .all()
  )


def create_tfmodel(db: Session, model: TFModel):

