from fastapi import APIRouter
from controllers.user import handle_get_users, handle_create_user
from schemas.user import UserCreate, UserResponse
from typing import List

router = APIRouter()

@router.get("", response_model=List[UserResponse])
async def get_all_users():
    return handle_get_users()

@router.post("", response_model=UserResponse)
async def create_user(user: UserCreate):
    return handle_create_user(user)
