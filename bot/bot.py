import asyncpg
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from tgbot.utils.register_handlers import register_handlers
from tgbot.data import config
from tgbot.middlewares.db import DbMiddleware

logger = logging.getLogger(__name__)


async def create_pool(user, password, host, port, dp):
    return await asyncpg.create_pool(user=user,
                                     password=password,
                                     host=host,
                                     port=port,
                                     database=dp
                                     )


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    storage = RedisStorage2(
        db=config.REDIS_DB_FSM,
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        password=config.REDIS_PASSWORD
    )

    pool = await create_pool(
        user=config.PG_USERNAME,
        password=config.PG_PASSWORD,
        host=config.PG_HOST,
        port=config.PG_PORT,
        dp=config.PG_DB
    )
    bot = Bot(
        token=config.BOT_TOKEN,
        parse_mode="html"
    )
    dp = Dispatcher(bot, storage=storage)
    dp.middleware.setup(DbMiddleware(pool))
    register_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
