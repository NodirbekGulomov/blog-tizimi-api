from fastapi import FastAPI

from app.routers.auth_router import router as auth_router
from app.routers.post_router import router as post_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(post_router)
