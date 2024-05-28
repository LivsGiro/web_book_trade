from fastapi import HTTPException, status

class DataBaseTransactionException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database transaction error")