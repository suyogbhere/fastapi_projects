from user.models import create_tables
import asyncio


async def main():
    #Create Table
    await create_tables()

    #Create Data
    # await create_user("suyog","suyogbhere@gmail.com")
    # await create_user("suraj","surajbhere@gmail.com")

 
asyncio.run(main())