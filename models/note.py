import datetime
from enum import unique
from sqlalchemy import Column,Integer,String,DateTime,Date,Float,Text
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from models import db




class Note(Base):
    __tablename__ = "note"
    id = Column(Integer,primary_key=True)
    content = Column(Text,nullable=False)
    slug_url = Column(String(255),nullable=False,unique=True)
    
    created_at = Column(DateTime, default=datetime.datetime.utcnow()+datetime.timedelta(hours=7))
    updated_at = Column(DateTime, default=datetime.datetime.utcnow()+datetime.timedelta(hours=7))
    
Base.metadata.create_all(db.engine)