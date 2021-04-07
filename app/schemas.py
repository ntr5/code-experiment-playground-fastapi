from typing import List
from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    complete: bool
    


class TodoCreate(TodoBase):    
    owner_id: int

    class Config: 
        schema_extra ={
            "example": {
                "title": "Buy Milk",
                "complete": False,
                "owner_id": 1
            }
        }


class Todo(TodoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    todos: List[Todo] = []

    class Config:
        orm_mode = True
