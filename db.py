from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    pool_size = 10,
    max_overflow = 20,
    pool_pre_ping = True,
    pool_recycle = 1800,
    echo = False,
)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session