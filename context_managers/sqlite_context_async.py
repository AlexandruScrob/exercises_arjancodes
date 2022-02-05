import asyncio
import logging
import aiosqlite

from constants import DB_PATH


async def main():
    logging.basicConfig(level=logging.INFO)
    async with aiosqlite.connect(DB_PATH) as db:
        # async with (
        # aiosqlite.connect("application.db") as db,
        # db.execute("SELECT * FROM blogs") as cursor,
        # ):
        async with db.execute("SELECT * FROM blogs") as cursor:
            # cursor = await db.execute("SELECT * FROM blogs")
            logging.info(await cursor.fetchall())


if __name__ == "__main__":
    asyncio.run(main())
