from pydantic import BaseModel

class Control(BaseModel):
    fromUser: str
    command: str