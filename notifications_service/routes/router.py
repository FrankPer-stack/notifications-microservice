from fastapi import APIRouter
from .notifications.endpoint import router as notifications_router

central_router = APIRouter()
central_router.include_router(router=notifications_router)
 
