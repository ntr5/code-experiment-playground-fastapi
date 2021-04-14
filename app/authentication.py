from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_401_UNAUTHORIZED
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm.session import Session
from app.database import get_db
from app import schemas, crud

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Hash():
    def hash_password(password: str):
        return pwd_cxt.hash(password)

    def verify_password(plain_password, hashed_password) -> bool:
        return pwd_cxt.verify(plain_password, hashed_password)


def get_current_user(data: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenicate": "Bearer"}
    )
    token_data = verify_token(data, credentials_exception)
    db_user = crud.get_user(db, user_id=token_data.id)
    return db_user


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('username')
        id: int = payload.get('id')
        if username is None:
            raise credentials_exception
        if id is None: 
            raise credentials_exception
        token_data = schemas.TokenData(username=username, id=id)
        return token_data
    except JWTError:
        raise credentials_exception