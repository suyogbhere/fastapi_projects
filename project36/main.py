from tables import create_table, drop_table
import asyncio
from services import *



async def main():
    ##Create table
    # await create_table()

    ## Create Data
    await create_user("Suyog","suyogbhere55@gmail.com")


asyncio.run(main())


