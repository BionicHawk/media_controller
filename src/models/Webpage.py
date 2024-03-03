from pydantic import BaseModel

class Webpage(BaseModel):
    fromUser: str
    url: str