import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
print(f"Using database URL: {DATABASE_URL}")

Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=False)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

def drop_tables(connection):
    Base.metadata.drop_all(bind=connection)

def create_tables(connection):
    Base.metadata.create_all(bind=connection)