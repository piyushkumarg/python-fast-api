from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True