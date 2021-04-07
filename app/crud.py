from sqlalchemy.orm import Session
from . import models, schemas
from app.authentication import Hash


def create_todo(db: Session, todo: schemas.TodoCreate):
    new_todo = models.Todo(**todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def create_user(db: Session, user: schemas.UserCreate):
    new_user = models.User(username=user.username, hashed_password=Hash.hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()