from app.db.database import Base, engine
from app.models import user, bug

Base.metadata.create_all(bind=engine)
