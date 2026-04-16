from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.features.auth.router import router as auth_router

app = FastAPI(
    title="Internal Team Workspace API",
    description="Backend for internal team management",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "Internal Team Workspace API is running"}
