from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///./sqlite.db"

engine = create_engine(DATABASE_URL, echo=True)


sessionlocal = sessionmaker(bind=engine, expire_on_commit=False)