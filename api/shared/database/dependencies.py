from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from api.shared.database.connection import async_session

async def get_db():
    """
    Provides a database session.

    Yields:
        AsyncSession: The database session.
    """
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
            
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session