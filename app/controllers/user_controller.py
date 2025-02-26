from fastapi import HTTPException
from app.services.user_service import get_all_users, create_user
from app.schemas.user_schema import UserCreate, UserResponse
from typing import List

def handle_get_users() -> List[UserResponse]:
    users = get_all_users()
    return users

def handle_create_user(user: UserCreate) -> UserResponse:
    new_user = create_user(user.name)
    return new_user
