import asyncio
from app.core.db import AsyncSessionLocal
from app.features.users.repository import UserRepository
from app.features.users.schemas import UserCreate
from app.features.users.models import UserRole

async def seed_admin():
    async with AsyncSessionLocal() as db:
        repo = UserRepository(db)
        
        # Check if admin already exists
        admin_email = "admin@example.com"
        existing_admin = await repo.get_by_email(admin_email)
        
        if not existing_admin:
            admin_in = UserCreate(
                email=admin_email,
                full_name="Initial Admin",
                password="adminpassword123",  # In a real app, this should be changed immediately
                role=UserRole.ADMIN,
                is_active=True
            )
            await repo.create(admin_in)
            print(f"Admin user created: {admin_email}")
        else:
            print(f"Admin user already exists: {admin_email}")

if __name__ == "__main__":
    asyncio.run(seed_admin())
