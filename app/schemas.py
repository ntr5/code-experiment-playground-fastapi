from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    complete: bool

class Todo(TodoBase):
    id: int

    class Config:
        orm_mode = True
