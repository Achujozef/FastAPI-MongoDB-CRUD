from pydantic import BaseModel

class Todo(BaseModel):
    name:str
    descriptions:str
    complete:bool
    