import os
import jwt
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Union
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()

#SECRET_KEY = os.getenv("123")
#ALGORITHM = os.getenv("ALGORITHM", "HS256")
SECRET_KEY = "123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

def create_access_token(data: Dict[str, Union[str, int]], expires_delta: Optional[timedelta] = None) -> str:
    """
    Creates a JWT token with the given data and expiration time.

    Args:
        data (Dict[str, Union[str, int]]): The data to encode in the token.
        expires_delta (Optional[timedelta], optional): The expiration time for the token. Defaults to None.

    Returns:
        str: The encoded JWT token.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> Optional[Dict[str, Union[str, int]]]:
    """
    Verifies the given JWT token and returns the decoded data.

    Args:
        token (str): The JWT token to verify.

    Returns:
        Optional[Dict[str, Union[str, int]]]: The decoded token data if the token is valid, None otherwise.
    
    Raises:
        HTTPException: If the token is invalid, expired, or has invalid claims.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTClaimsError:
        raise HTTPException(status_code=401, detail="Invalid token claims")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
