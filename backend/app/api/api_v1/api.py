from fastapi import APIRouter
from app.api.api_v1.endpoints import login, user, chatbot, intents, entity
api_router = APIRouter()

api_router.include_router(login.router, tags=['login_form'])
api_router.include_router(user.router, tags=['user'])
api_router.include_router(chatbot.router, tags=['chatbot'])
api_router.include_router(intents.router, tags=['intents'])
api_router.include_router(entity.router, tags=['entities'])