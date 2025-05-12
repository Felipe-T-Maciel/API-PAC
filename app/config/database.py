from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def create_db_if_not_exists():
  DATABASE_URL = "postgresql://postgres:root@localhost:5432/"
  engine = create_engine(DATABASE_URL)
  try:
    with engine.connect() as connection:
      connection.execution_options(isolation_level="AUTOCOMMIT").execute(
    text("CREATE DATABASE teste ENCODING 'UTF8' TEMPLATE template1")
)
    engine.clear_compiled_cache()
  except:
    pass  

create_db_if_not_exists()
DATABASE_URL = "postgresql://postgres:root@localhost:5432/teste"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()