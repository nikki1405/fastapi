from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import User
from app.auth_utils import create_access_token, pwd_context  # adjust imports

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_credentials.username).first()

    if not user or not pwd_context.verify(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({
        "sub": user.username,
        "is_admin": user.is_admin
    })

    return {"access_token": access_token, "token_type": "bearer"}
