import pytest
import asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from api.database.connection import Base
from api.main import app

# Definindo a URL do banco de dados
DATABASE_URL = "postgresql+asyncpg://root:1234@localhost:5439/book_trade_test"

@pytest.fixture(scope='session')
def event_loop(event_loop_policy):
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='function', autouse=True)
async def setup_database():
    engine = create_async_engine(DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    
    async with async_session() as session:
        yield session
        
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()

@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
