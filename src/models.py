from sqlalchemy import Column, Integer, String
from .database import Base


class TFModel(Base):
    __tablename__ = "tfmodels"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    file = Column(String, index=True)