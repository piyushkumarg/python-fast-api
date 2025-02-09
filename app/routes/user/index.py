from fastapi import APIRouter, HTTPException

user_router = APIRouter()

# Temporary in-memory storage for example
fake_users_db = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"}
]

@user_router.get("")
async def get_all_users():
    return {
        "message": "Users retrieved successfully",
        "data": fake_users_db
    }

@user_router.post("")
async def create_user(name: str):
    new_user = {
        "id": len(fake_users_db) + 1,
        "name": name
    }
    fake_users_db.append(new_user)
    return {
        "message": "User created successfully",
        "data": new_user
    }