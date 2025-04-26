from fastapi import APIRouter
from typing import List
from schemas.user import User
from models.user import users
from core.db import database
from utils import time_check

router = APIRouter()

@router.get("/", response_model=List[User])
@time_check 
async def get_users():
    query = users.select()
    users_list = await database.fetch_all(query)
    return users_list
