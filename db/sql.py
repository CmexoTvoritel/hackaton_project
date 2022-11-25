import asyncio
import asyncpg


async def create_db():
    create_db_command = open("db_dump.sql", "r", encoding="utf-8").read()
    conn: asyncpg.Connection = await asyncpg.connect(user="admin",
                                                     password="admin",
                                                     host="localhost",
                                                     port="5432",
                                                     database="bot-hackaton"
                                                     )
    await conn.execute(create_db_command)
    await conn.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
