import pytest
import uuid
import asyncio
from sqlalchemy.dialects.postgresql import UUID
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_find_all_users_not_found(client: AsyncClient) -> None:
    """
    Test the behavior when no users are found.

    This test checks that the endpoint returns a 404 status code
    and the correct error message when no users are found.
    """
    response = await client.get("/users/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User not found"}

@pytest.mark.asyncio
async def test_find_all_users_pagination(client: AsyncClient) -> None:
    """
    Test the retrieval of all users with pagination.

    This test checks that the endpoint returns a 200 status code
    and the correct list of users on pagination.
    """
    user1 = {
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
    
    user2 = {
        "cpf": "12345678912",
        "email": "user1@example2.com",
        "whatsapp": "14991000002",
        "name": "UserExample1",
        "password": "securepassword",        
        "sex": "M",
        "date_birth": "1990-01-01",
        "notification_email": True,
        "notification_whats": True,
        "cep": "18654000"
    }
    
    user3 = {
        "cpf": "12345678913",
        "email": "user1@example3.com",
        "whatsapp": "14991000003",
        "name": "UserExample1",
        "password": "securepassword",        
        "sex": "M",
        "date_birth": "1990-01-01",
        "notification_email": True,
        "notification_whats": True,
        "cep": "18654000"
    }
    
    response1 = await client.post("/users/", json=user1)
    assert response1.status_code == status.HTTP_201_CREATED
    response2 = await client.post("/users/", json=user2)
    assert response2.status_code == status.HTTP_201_CREATED
    response3 = await client.post("/users/", json=user3)
    assert response3.status_code == status.HTTP_201_CREATED
    
    response = await client.get("/users/?skip=0&limit=2")
    assert response.status_code == status.HTTP_200_OK

    body = response.json()
    assert isinstance(body, list)
    assert len(body) == 2

    emails = [user["email"] for user in body]
    assert user1["email"] in emails
    assert user2["email"] in emails

@pytest.mark.asyncio
async def test_find_all_users(client: AsyncClient) -> None:
    """
    Test the retrieval of all users.

    This test checks that the endpoint returns a 200 status code.
    """
    user1 = {
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
    
    user2 = {
        "cpf": "12345678912",
        "email": "user1@example2.com",
        "whatsapp": "14991000002",
        "name": "UserExample1",
        "password": "securepassword",        
        "sex": "M",
        "date_birth": "1990-01-01",
        "notification_email": True,
        "notification_whats": True,
        "cep": "18654000"
    }
    
    user3 = {
        "cpf": "12345678913",
        "email": "user1@example3.com",
        "whatsapp": "14991000003",
        "name": "UserExample1",
        "password": "securepassword",        
        "sex": "M",
        "date_birth": "1990-01-01",
        "notification_email": True,
        "notification_whats": True,
        "cep": "18654000"
    }
    
    response1 = await client.post("/users/", json=user1)
    assert response1.status_code == status.HTTP_201_CREATED
    response2 = await client.post("/users/", json=user2)
    assert response2.status_code == status.HTTP_201_CREATED
    response3 = await client.post("/users/", json=user3)
    assert response3.status_code == status.HTTP_201_CREATED
    
    response = await client.get("/users/")
    assert response.status_code == status.HTTP_200_OK

    body = response.json()
    assert isinstance(body, list)
    assert len(body) == 3

    emails = [user["email"] for user in body]
    assert user1["email"] in emails
    assert user2["email"] in emails

