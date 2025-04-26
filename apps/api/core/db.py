from utils.logger import logger
from sqlalchemy import MetaData, create_engine
from . import config
import databases
from utils import time_check

database = databases.Database(config.DB_URL)
engine = create_engine(config.DB_URL)
metadata = MetaData()

@time_check 
def reset_database():
    try:
        metadata.drop_all(engine) 
        metadata.create_all(engine)  
    except Exception as e:
        logger.error(f"Error during database reset: {str(e)}")
