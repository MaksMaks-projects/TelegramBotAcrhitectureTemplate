from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")

host = env.str("DB_HOST")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")

PG_HOST = env.str("PG_HOST")
PG_PASSWORD = env.str("PG_PASSWORD")
