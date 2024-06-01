import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

#DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_URL = "postgresql+asyncpg://root:1234@localhost:5439/book_trade_test"

Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=False)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)