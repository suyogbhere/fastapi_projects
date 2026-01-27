from tables import create_table, drop_table
import asyncio
from services import *



async def main():
    ##Create table
    # await create_table()

    ## Create Data
    # await create_user("Suyog","suyogbhere55@gmail.com")
    # await create_user("Suraj","surajbhere55@gmail.com")

    ##Read Data
    # print(await get_user_by_id(1))
    # print(await get_all_users())

    ## Update Data
    # await update_user_email(2,"surajbhere@gmail.com")

    ##Delete Data
    await delete_user(2)

asyncio.run(main())


