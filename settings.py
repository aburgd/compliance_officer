from dotenv import load_dotenv

load_dotenv()

import os

CLIENT_TOKEN = os.getenv("CLIENT_TOKEN")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_LOCN = os.getenv("DB_LOCN")
DB_NAME = os.getenv("DB_NAME")
