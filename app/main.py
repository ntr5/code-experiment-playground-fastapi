from fastapi import FastAPI
from . import models
from .database import engine
from .routers import todo, user, authentication as auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(todo.router)
app.include_router(user.router)



# @app.post("/create_todo/", response_model=schemas.Todo)
# def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(authentication.get_current_user)):
#     return crud.create_todo(db, todo=todo, user_id=current_user.id)


# @app.post("/create_user", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     return crud.create_user(db, user=user)


# @app.get("/get-user/{user_id}", response_model=schemas.User)
# def get_user(user_id: int, db: Session = Depends(get_db)):
#     return crud.get_user(db, user_id=user_id)