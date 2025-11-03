from db import engine
from tables import users , posts
from sqlalchemy import text


## Using RAW SQL (Insert)
def raw_sql_insert():
    with engine.connect() as conn:
        stmt = text("""
                    INSERT INTO users(name, email)
                    VALUES(:name, :email)
                    """)
        conn.execute(stmt, {"name":"Suyog", "email":"suyog@gmail.com"})
        conn.commit()
