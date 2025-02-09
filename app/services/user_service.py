from typing import List, Dict

# Temporary in-memory storage
fake_users_db: List[Dict] = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"}
]

def get_all_users():
    return fake_users_db

def create_user(name: str):
    new_user = {
        "id": len(fake_users_db) + 1,
        "name": name
    }
    fake_users_db.append(new_user)
    return new_user
