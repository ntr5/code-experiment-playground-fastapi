from sqlalchemy.orm import Session
from . import models, schemas


def create_todo(db: Session, todo: schemas.TodoBase):
    new_todo = models.Todo(**todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo