from config import config
from urllib.parse import quote
import datetime
from sqlalchemy import create_engine, true
from sqlalchemy import Column,Integer,String,DateTime,Date,Float,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()


db_host = config.settings.db_host
db_name = config.settings.db_name
db_user = config.settings.db_user
db_pass = config.settings.db_pass

engine = create_engine(f'mysql+pymysql://{db_user}:{quote(db_pass)}@{db_host}/{db_name}')




Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db():
    db = Session()
    print(db)
    try:
        yield db
    finally:
        db.close()

# 