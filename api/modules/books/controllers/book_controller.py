from uuid import UUID
from typing import List, Optional
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.modules.books.services.book_service import BookService
from api.modules.books.schemas.book_schema import BookResponsePublic
from api.shared.database.dependencies import get_db
from api.shared.database.dependencies import get_current_user

class BookController:
    def __init__(self, session: AsyncSession = Depends(get_db), user_id: Optional[UUID] = Depends(get_current_user)):
        self.session = session
        self.user_id = user_id
        self.book_service = BookService(session)
        
    async def create_new_book(self, data_book) -> BookResponsePublic:
        if not self.user_id:
            raise HTTPException(status_code=401, detail="Authentication required")
        new_book = await self.book_service.create_book(self.user_id, data_book)
        
        return new_book
    
    async def get_all_books(self, skip: int = 0, limit: int = 10) -> List[BookResponsePublic]:
        books = await self.user_service.get_all_books(skip=skip, limit=limit)

        return books