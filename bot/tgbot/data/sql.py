import asyncio
import asyncpg
from config import PG_USERNAME, PG_PASSWORD, PG_HOST, PG_PORT, PG_DB, DB_DUMP_PATH


async def create_db():
    create_db_command = open(DB_DUMP_PATH, "r", encoding="utf-8").read()
    conn: asyncpg.Connection = await asyncpg.connect(user=PG_USERNAME,
                                                     password=PG_PASSWORD,
                                                     host=PG_HOST,
                                                     port=PG_PORT,
                                                     database=PG_DB
                                                     )
    await conn.execute(create_db_command)
    await conn.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
