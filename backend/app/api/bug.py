from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.bug import Bug
from app.schemas.bug import BugCreate, BugOut, BugUpdate, BugTextInput 
from app.core.security import get_current_user, get_current_admin
from app.services.ml_predict import predict_bug_info

router = APIRouter()

# Create a bug report
@router.post("/", response_model=BugOut)
def create_bug(
    bug: BugCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    predictions = predict_bug_info(bug.description)
    new_bug = Bug(
        title=bug.title,
        description=bug.description,
        reporter=current_user.username,
        priority=predictions["priority"],
        bug_type=predictions["type"],
        category=bug.category  # Make sure this matches your Bug model
    )
    db.add(new_bug)
    db.commit()
    db.refresh(new_bug)
    return new_bug

# Get bugs: admin sees all, user sees their own
@router.get("/", response_model=List[BugOut])
def get_bugs(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if hasattr(current_user, "is_admin") and current_user.is_admin:
        return db.query(Bug).all()
    return db.query(Bug).filter(Bug.reporter == current_user.username).all()

# Assign or update a bug (admin only)
@router.put("/{bug_id}")
def update_bug(
    bug_id: int,
    bug_update: BugUpdate,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    bug = db.query(Bug).filter(Bug.id == bug_id).first()
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
    for field, value in bug_update.dict(exclude_unset=True).items():
        setattr(bug, field, value)
    db.commit()
    db.refresh(bug)
    return {"message": "Bug updated", "bug": bug}

# Predict bug priority/type
@router.post("/predict")
def predict_route(input: BugTextInput = Body(...)):
    result = predict_bug_info(input.text)
    return {"predicted_priority": result["priority"]}
