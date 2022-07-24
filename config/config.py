import os
from typing import Optional
from pydantic import BaseSettings

class Settings(BaseSettings):
    port:int
    db_host:str
    db_name:str
    db_user:str
    db_pass:str
    
    
    class Config:
        env_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),'.env')

settings = Settings()
