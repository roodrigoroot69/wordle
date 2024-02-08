from common.infra.auth.token import create_jwt_token
from common.infra.database import get_db
from common.infra.models import User
from wordle.infra.models.user import UserRequest

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/login/")
def login(user_request: UserRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_request.username).first()
    if not user or not pwd_context.verify(user_request.password, user.password):
        return None
    return create_jwt_token(
        data={"user_id": user.id, "username": user.username}, expires_minutes=30
    )


@router.post("/users/", status_code=201)
def create_user(user: UserRequest, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
