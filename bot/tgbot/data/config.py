from environs import Env
from os import sep

env = Env()
env.read_env()

# Bot
BOT_TOKEN = env.str("BOT_TOKEN")
# PostgreSQL
PG_USERNAME = env.str("PG_USERNAME")
PG_PASSWORD = env.str("PG_PASSWORD")
PG_HOST = env.str("PG_HOST")
PG_PORT = env.int("PG_PORT")
PG_DB = env.str("PG_DB_NAME")
# REDIS
REDIS_HOST = env.str("REDIS_HOST")
REDIS_PORT = env.int("REDIS_PORT")
REDIS_PASSWORD = env.str("REDIS_PASSWORD")
REDIS_DB_FSM = env.int("REDIS_DB_FSM")
REDIS_DB_JOBSTORE = env.int("REDIS_DB_JOBSTORE")
