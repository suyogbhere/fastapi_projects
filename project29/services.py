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



## Using Raw SQL ( SELECT )
def raw_sql_example():
    with engine.connect() as conn:
        stmt = text("SELECT * FROM users")
        result = conn.execute(stmt)
        return result
    

## Using Raw SQL ( SELECT where)
def raw_sql_example_where():
    with engine.connect() as conn:
        stmt = text("SELECT * FROM users WHERE email = :email")
        result = conn.execute(stmt, {"email":"suyog@gmail.com"}).first()
        return result
    

