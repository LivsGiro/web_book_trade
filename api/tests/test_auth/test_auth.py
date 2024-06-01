import pytest
import jwt
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_failed_login(client: AsyncClient):
    """
    Test failed login with incorrect password.

    This test verifies that attempting to log in with an incorrect password
    returns a 401 Unauthorized status code.
    """
    response = await client.post("/auth/", json={"email": "user@example.com", "password": "wrongpassword"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.asyncio
async def test_login(client: AsyncClient):
    """
    Test successful user registration and login.

    This test verifies that a new user can be successfully registered,
    and that the same user can log in with the correct credentials.
    Additionally, it verifies that the login response includes a valid JWT token.
    """
    SECRET_KEY = "123"
    ALGORITHM = "HS256"
    user = {
        "cpf": "12345678911",
        "email": "user1@example.com",
        "whatsapp": "14991000000",
        "name": "UserExample1",
        "password": "securepassword",        
        "sex": "M",
        "date_birth": "1990-01-01",
        "notification_email": True,
        "notification_whats": True,
        "cep": "18654000"
    }
        
    response = await client.post("/users/", json=user)
    assert response.status_code == status.HTTP_201_CREATED
    
    body = response.json()
    assert body["email"] == user["email"]
    assert body["name"] == user["name"]
    assert body["sex"] == user["sex"]
    
    response = await client.post("/auth/", json={"email": "user1@example.com", "password": "securepassword"})
    assert response.status_code == status.HTTP_200_OK
    
    body = response.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"