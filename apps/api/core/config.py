from dotenv import load_dotenv
import os 

load_dotenv(dotenv_path=".env")

class Config:
    DB_URL = os.getenv("DB_URL")

config = Config()

