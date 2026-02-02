from models import create_tables, drop_tables
import asyncio
from services import *

async def main():
    #Create Table
    # await create_tables()

    #Create Data
    # await create_user("suyog","suyogbhere@gmail.com")
    # await create_user("suraj","surajbhere@gmail.com")

    ##Read Data
    # print(await get_user_by_id(2))
    # print(await get_all_users())


    #Update the data
    await update_user_email(1,"suyogbhere55@gmail.com")

asyncio.run(main())