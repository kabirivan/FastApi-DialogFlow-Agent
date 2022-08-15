from fastapi import APIRouter
from app.api.api_v1.endpoints import login, user
api_router = APIRouter()

api_router.include_router(login.router, tags=['login_form'])
api_router.include_router(user.router, tags=['user'])