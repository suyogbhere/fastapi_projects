# Create engine

from sqlalchemy import create_engine
DATABASE_URL = "sqlite:///./sqlite.db"

##  echo true  is for debugging purpose
engine = create_engine(DATABASE_URL, echo=True)