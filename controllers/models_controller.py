# Controladores para os models gerados na API
from fastapi import APIRouter
from usecases.models_usecases import (
    get_all_models
)

models_router = APIRouter(
    prefix="/v1/models",
    tags=["models"])


@models_router.get("/")
async def get_all():
    return get_all_models()
