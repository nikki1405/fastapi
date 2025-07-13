from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from app.models.bug import Bug
from app.models.user import User
from app.db.database import get_db
from app.schemas.bug import BugCreate, BugOut, BugTextInput
from app.services.ml_predict import predict_bug_info
from app.core.security import get_current_user
from typing import List

router = APIRouter(prefix="/bugs", tags=["bugs"])

@router.post("/predict")
def predict_bug_priority(data: BugTextInput = Body(...)):
    result = predict_bug_info(data.text)
    return {"predicted_priority": result["priority"]}

@router.post("/", response_model=BugOut)
def report_bug(
    bug: BugCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_bug = Bug(
        title=bug.title,
        description=bug.description,
        category=bug.category,
        priority=bug.priority,
        reported_by=current_user.id,
        status="Open",
    )
    db.add(new_bug)
    db.commit()
    db.refresh(new_bug)
    return new_bug

@router.get("/", response_model=List[BugOut])
def get_all_bugs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return db.query(Bug).all()
