from pydantic import BaseModel
class note(BaseModel):
    content:str
    slug_url:str