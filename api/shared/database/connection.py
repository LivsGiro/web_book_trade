import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

env = os.getenv("ENV", "development")
if env == "production":
    load_dotenv(".env.prod")
elif env == "testing":
    load_dotenv(".env.test")
else:
    load_dotenv(".env.dev")

DATABASE_URL = os.getenv("DATABASE_URL")
print(f"Using database URL: {DATABASE_URL}")

Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=False)
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
