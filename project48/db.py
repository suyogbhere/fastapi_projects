from sqlmodel import create_engine, SQLModel


DATABASE_URL = "sqlite:///sqlite.db"

engine = create_engine(DATABASE_URL, echo= True)


# SQLModel.metadata.create_all()



def create_tables():
    SQLModel.metadata.create_all(engine)