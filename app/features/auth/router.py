from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from app.core.dependencies import get_db, get_current_user
from app.features.auth.schemas import TokenResponse
from app.features.auth.service import AuthService
from app.features.users.schemas import UserRead
from app.features.users.models import User

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=TokenResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    service = AuthService(db)
    return await service.authenticate_user(form_data)

@router.get("/me", response_model=UserRead)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user
