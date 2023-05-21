from .schemas import TFModel
from .database import get_db
from .usecases import find_all_users
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

# Router para os TFModels
tfmodels_router = APIRouter(
    prefix="/v1/models",
    tags=["models"]
)

@tfmodels_router.get("/", response_model=list[TFModel])
def get_all_users(db: Session = Depends(get_db)):
    return find_all_users(db)