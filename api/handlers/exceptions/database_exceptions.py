from fastapi import HTTPException, status

class DataBaseTransactionException(HTTPException):
    def __init__(self, detail: str = 'Database transaction error'):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
        
class SQLAlchemyErrorException(HTTPException):
    def __init__(self, detail: str = 'Database transaction failed'):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)