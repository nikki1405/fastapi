from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Bug(Base):
    __tablename__ = "bugs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    reporter = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    bug_type = Column(String, nullable=True)
    category = Column(String, nullable=True)  # <-- Add this line
    status = Column(String, default="Open")  # Open, In Progress, Resolved
    assigned_to = Column(Integer, ForeignKey("users.id"))

    developer = relationship("User")
