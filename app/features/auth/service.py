from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from app.features.users.repository import UserRepository
from app.features.auth.schemas import TokenResponse
from app.core.auth import verify_password, create_access_token

class AuthService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.user_repo = UserRepository(db)

    async def authenticate_user(self, form_data: OAuth2PasswordRequestForm) -> TokenResponse:
        user = await self.user_repo.get_by_email(form_data.username)
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Inactive user"
            )

        access_token = create_access_token(data={"sub": user.email})
        return TokenResponse(access_token=access_token)
