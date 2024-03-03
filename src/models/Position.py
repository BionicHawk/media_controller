from pydantic import BaseModel

class Position(BaseModel):
    fromUser: str
    x: float
    y: float
    z: float
    