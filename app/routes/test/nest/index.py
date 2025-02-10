from fastapi import APIRouter

router = APIRouter()

@router.get("")
async def get_nest_test():
    return  {"message": "Welcome to Nested Test API"}
    