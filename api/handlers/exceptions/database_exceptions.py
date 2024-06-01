from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError, DataError

class DataBaseTransactionException(HTTPException):
    def __init__(self, exception: Exception):
        error_message = "An unexpected error occurred in the database transaction."
        if isinstance(exception, IntegrityError):
            error_message = f"Integrity constraint violated: {exception.orig}"
        elif isinstance(exception, OperationalError):
            error_message = f"Operational error in database transaction: {exception.orig}"
        elif isinstance(exception, DataError):
            error_message = f"Data formatting error in database operation: {exception.orig}"
        elif isinstance(exception, SQLAlchemyError):
            error_message = f"Database transaction failed: {str(exception)}"

        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error_message)
        
