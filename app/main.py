from typing import Optional
from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create_todo/", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo=todo)


@app.get("/{todo_id}")
def hello(todo_id: int, name: Optional[str] = None, email: Optional[str] = Query(None, max_length=50)):
    return {"todo_id": todo_id, "name": name, "email": email}
