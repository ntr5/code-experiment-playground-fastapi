from sqlalchemy.orm import Session
from . import models, schemas
from app.authentication import Hash


def create_todo(db: Session, todo: schemas.TodoCreate, user_id: int):
    new_todo = models.Todo(**todo.dict(), owner_id=user_id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def create_user(db: Session, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user is None:
        new_user = models.User(username=user.username, hashed_password=Hash.hash_password(user.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    return None


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()