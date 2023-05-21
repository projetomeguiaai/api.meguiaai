from pydantic import BaseModel


# Schemas para validação dos dados
class TFModel(BaseModel):
    id: int
    name: str
    file: str

    class Config:
        orm_mode = True


class CreateTFModel(BaseModel):
    name: str
    file: str

    class Config:
        orm_mode = True
