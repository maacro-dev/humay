from fastapi import FastAPI
from core import config
from core.db import database, reset_database
from routers.user import router as user_router

app = FastAPI()
app.include_router(user_router, prefix="/users", tags=["users"])

@app.on_event("startup")
async def startup():
    reset_database()
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

