from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


# Carrega as envs do .env
load_dotenv()

# Cria engine com link do postgres
engine = create_engine(os.getenv("DB_URL"))

# Cria uma sessão da ORM
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma base para os models
Base = declarative_base()

# Dependencia que retorna o db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()