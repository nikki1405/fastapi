from pydantic import BaseModel
from typing import Optional

# Used for predicting priority
class BugTextInput(BaseModel):
    text: str


# Used when creating a bug (from frontend)
class BugCreate(BaseModel):
    title: str
    description: str
    category: str
    priority: str


# Used for admin updates
class BugUpdate(BaseModel):
    priority: Optional[str]
    bug_type: Optional[str]
    status: Optional[str]
    assigned_to: Optional[int]


# Used when sending bug data to frontend
class BugOut(BaseModel):
    id: int
    title: str
    description: str
    category: Optional[str] = None
    priority: Optional[str] = None
    bug_type: Optional[str] = None
    status: Optional[str] = None
    reporter: Optional[str] = None
    assigned_to: Optional[int] = None

    class Config:
        orm_mode = True
