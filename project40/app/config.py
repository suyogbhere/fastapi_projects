from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
db_path = os.path.join(BASE_DIR,"sqlite.db")

DATABASE_URL = f"sqlite:///{db_path}"


# DATABASE_URL = "sqlite:///sqlite.db"

engine = create_engine(DATABASE_URL, echo= True)


Sessionlocal = sessionmaker(bind=engine, expire_on_commit=False)

