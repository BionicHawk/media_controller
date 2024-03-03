from pydantic import BaseModel

class Typed(BaseModel):
    fromUser: str
    query: str
    