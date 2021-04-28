from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, authentication
from app.database import get_db
router = APIRouter()


@router.post("/create-todo", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(authentication.get_current_user)):
    return crud.create_todo(db, todo=todo, user_id=current_user.id)
