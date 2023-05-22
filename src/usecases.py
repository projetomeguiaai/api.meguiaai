from sqlalchemy.orm import Session
from . import models
from .helpers.tensorflow_helper import *
from .schemas import *
import base64


# Obtem todos os models
def find_all_tfmodels(db: Session, skip: int = 0, limit: int = 100):
  return (
    db.query(models.TFModel)
    .offset(skip)
    .limit(limit)
    .all()
  )


# Seleciona um model dado o ID
def find_tfmodel_by_id(db: Session, id: int):
  return (
    db.query(models.TFModel)
    .filter_by(id=id)
    .first()
  )


# Adiciona um model encodificado em Base64
def add_tfmodel(db: Session, model: AddTFModel):
  ## Abre o caminho do arquivo e lê em Bytes
  tfmodel = open(model.model_path, "rb")

  ## Converte o arquivo aberto em Base64
  model_b64 = base64.b64encode(tfmodel.read())

  ## Cria um novo TFModel instância do model TFModel
  new_model = models.TFModel(
    name=model.name, # --> Nome do model
    model=model_b64, # --> Modelo aberto
    labels=model.labels # --> Labels da predição - que é separada
  )

  db.add(new_model) # --> Adiciona modificações no histórico
  db.commit() # --> Adiciona no banco
  db.refresh(new_model) # --> Recarrega o banco

  ## Retorna o model criado
  return new_model


# Faz uma predição, dado o ID do model e o caminho da imagem
def predict_img(pred: ModelPredict, db: Session):
  ## Pega o model no banco pelo ID
  model = db.query(models.TFModel).filter_by(id=pred.model_id).first()

  ## Decodifica em Base64
  model_bin = base64.b64decode(model.model)

  ## Cria um arquivo na pasta com o nome do model
  tfmodel_path = f"./src/data/{model.name}.h5"

  ## Escreve os dados binarios no arquivo
  with open(tfmodel_path, "wb") as f:
    f.write(model_bin)

  ## Faz uma predição usando o helper
  prediction = predict(model=tfmodel_path, img_path=pred.img_path, labels=model.labels)

  ## Remove o arquivo do model
  os.remove(tfmodel_path)

  ## Finalmente, retorna a prediction
  return prediction
