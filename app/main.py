from fastapi import FastAPI
from contextlib import asynccontextmanager

from api import grass_finder, auth
from core.config import CONFIG
from database.connection import engine, AsyncSessionLocal
from database.crud import seed_grass
from database.base import Base
from database.models.grass_models import Grass
from database.models.users import User

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as session:
        await seed_grass(session)
    yield

app = FastAPI(
    title=CONFIG.PROJECT_NAME,
    version=CONFIG.PROJECT_VERSION,
    description="Grass Finder API",
    lifespan=lifespan
)

@app.get("/")
async def main():
    return {"message": "Hello World"}

app.include_router(grass_finder.router, prefix="/api")
app.include_router(auth.router, prefix="/api")