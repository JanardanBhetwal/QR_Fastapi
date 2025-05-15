from app.api.api_v1.routers import qr  # import qr
from fastapi import APIRouter

api_router = APIRouter()
# api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(qr.router, prefix="/utils", tags=["qr"])  # new
