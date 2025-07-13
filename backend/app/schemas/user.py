from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserLogin(UserBase):
    password: str
# This is used for admin user creation
class UserOut(UserBase):
    id: int
    is_admin: bool

    class Config:
        orm_mode = True
    