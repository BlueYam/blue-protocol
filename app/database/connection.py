from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.core.config import CONFIG

connect_args = {"check_same_thread": False} if "sqlite" in CONFIG.DB_URL else {}

engine = create_async_engine(CONFIG.DB_URL, connect_args=connect_args)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()