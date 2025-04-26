from sqlalchemy import MetaData, create_engine
from . import config
import databases

database = databases.Database(config.DB_URL)
engine = create_engine(config.DB_URL)
metadata = MetaData()

def reset_database():
    import models.user
    metadata.drop_all(engine)
    metadata.create_all(engine)







