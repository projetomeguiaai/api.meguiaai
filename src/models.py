from sqlalchemy import Column, Integer, String, ARRAY, LargeBinary
from .database import Base


# Cria um modelo para os tfmodels
class TFModel(Base):
    __tablename__ = "tfmodels"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    model = Column(LargeBinary)
    labels = Column(ARRAY(String))