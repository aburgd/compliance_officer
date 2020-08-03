from dotenv import load_dotenv

load_dotenv()

import os


def get_database_info():
    env = os.getenv("ENV")
    # 0 is dev, 1 is prod
    if env == "DEV":
        DB_USER = os.getenv("DB_USER_DEV")
        DB_PASS = os.getenv("DB_PASS_DEV")
        DB_HOST = os.getenv("DB_HOST_DEV")
    else:
        DB_USER = os.getenv("DB_USER")
        DB_PASS = os.getenv("DB_PASS")
        DB_HOST = os.getenv("DB_HOST")
    return (DB_USER, DB_PASS, DB_HOST)


CLIENT_TOKEN = os.getenv("CLIENT_TOKEN")
DB_NAME = os.getenv("DB_NAME")
db_info = get_database_info()
DB_USER = db_info[0]
DB_PASS = db_info[1]
DB_HOST = db_info[2]
