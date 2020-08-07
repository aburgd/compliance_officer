from dotenv import load_dotenv

load_dotenv()

import os

CLIENT_TOKEN = os.getenv("CLIENT_TOKEN")
DB_NAME = os.getenv("DB_NAME")
