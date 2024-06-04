import pytest
from httpx import AsyncClient
from sqlalchemy.dialects.postgresql import UUID
from fastapi import status

@pytest.mark.asyncio
async def test_create_new_user_duplicate_email(client: AsyncClient) -> None:
    """
    Test the creation of a user with a duplicate email.

    This test checks that creating a user with an existing email
    returns a 409 status code and the correct error message.
    """
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
    
    new_user = {
        "cpf": "12345678912",
        "email": "user1@example.com",
        "whatsapp": "14991000001",
        "name": "UserExample1",
        "password": "securepassword",        
        "sex": "M",
        "date_birth": "1990-01-01",
        "notification_email": True,
        "notification_whats": True,
        "cep": "18654000"
    }
    
    response1 = await client.post("/users/", json=user)
    assert response1.status_code == status.HTTP_201_CREATED
    
    response = await client.post("/users/", json=new_user)
    assert response.status_code == status.HTTP_409_CONFLICT
    
    body = response.json()
    assert body["detail"] == "User with this email already exists."
 
 
@pytest.mark.asyncio
async def test_create_new_user_duplicate_cpf(client: AsyncClient) -> None:
    """
    Test the creation of a user with a duplicate cpf.

    This test checks that creating a user with an existing cpf
    returns a 409 status code and the correct error message.
    """
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
    
    new_user = {
        "cpf": "12345678911",
        "email": "user1@example1.com",
        "whatsapp": "14991000001",
        "name": "UserExample1",
        "password": "securepassword",        
        "sex": "M",
        "date_birth": "1990-01-01",
        "notification_email": True,
        "notification_whats": True,
        "cep": "18654000"
    }
    
    response1 = await client.post("/users/", json=user)
    assert response1.status_code == status.HTTP_201_CREATED
    
    response = await client.post("/users/", json=new_user)
    assert response.status_code == status.HTTP_409_CONFLICT
    
    body = response.json()
    assert body["detail"] == "User with this cpf already exists."
    
    
@pytest.mark.asyncio
async def test_create_new_user_duplicate_whatsapp(client: AsyncClient) -> None:
    """
    Test the creation of a user with a duplicate whatsapp.

    This test checks that creating a user with an existing whatsapp
    returns a 409 status code and the correct error message.
    """
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
    
    new_user = {
        "cpf": "12345678912",
        "email": "user1@example2.com",
        "whatsapp": "14991000000",
        "name": "UserExample1",
        "password": "securepassword",        
        "sex": "M",
        "date_birth": "1990-01-01",
        "notification_email": True,
        "notification_whats": True,
        "cep": "18654000"
    }
    
    response1 = await client.post("/users/", json=user)
    assert response1.status_code == status.HTTP_201_CREATED
    
    response = await client.post("/users/", json=new_user)
    assert response.status_code == status.HTTP_409_CONFLICT
    
    body = response.json()
    assert body["detail"] == "User with this whastapp already exists."    


@pytest.mark.asyncio
async def test_create_new_user_invalid_email(client: AsyncClient) -> None:
    """
    Test creating a user with an invalid email format.

    Ensures that the API returns a 422 status code when an invalid email is provided.
    """
    user1 = {
        "cpf": "12345678911",
        "email": "user1", 
        "whatsapp": "14991000000",
        "name": "UserExample1",
        "password": "securepassword",
        "sex": "M",
        "date_birth": "1990-01-01",
        "notification_email": True,
        "notification_whats": True,
        "cep": "18654000"
    }

    response = await client.post("/users/", json=user1)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    body = response.json()
    assert body['detail'][0]['loc'][1] == 'email', "The error message should specify the 'email' field as problematic."
    assert 'value is not a valid email address' in body['detail'][0]['msg'], "The error message should clearly state that the email format is invalid."


@pytest.mark.asyncio
async def test_create_new_user_invalid_length_cpf(client: AsyncClient) -> None:
    """
    Test creating a user with an invalid CPF length.

    Ensures that the API returns a 422 status code when a CPF with incorrect length is provided.
    """
    user_details = {
        "cpf": "12345678",
        "email": "test@example.com",
        "whatsapp": "14991000000",
        "name": "UserExample1",
        "password": "securepassword",
        "sex": "M",
        "date_birth": "1990-01-01",
        "notification_email": True,
        "notification_whats": True,
        "cep": 18654000
    }

    response = await client.post("/users/", json=user_details)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    body = response.json()
    assert body['detail'][0]['loc'][1] == 'cpf', "The error message should specify the 'cpf' field as problematic."
    assert 'String should have at least 11 characters' in body['detail'][0]['msg'], "The error message should clearly state the CPF must be exactly 11 characters long."


@pytest.mark.asyncio
async def test_create_new_user(client: AsyncClient) -> None:
    """
    Test the creation of a user.

    returns a 201 status code and the correct message.
    """
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
    

"""
@pytest.mark.asyncio
async def test_create_new_user_invalid_cep(mock_get, client: AsyncClient):

    user1 = {
        "cpf": "12345678911",
        "email": "test@example.com",
        "whatsapp": "18654000",
        "name": "UserExample1",
        "password": "securepassword123",
        "sex": "M",
        "date_birth": "1990-01-01",
        "notification_email": True,
        "notification_whats": True,
        "cep": "00000000"  
    }

    response = await client.post("/users/", json=user1)
    assert response.status_code == 422

    body = response.json()
    assert 'cep' in body['detail'][0]['loc'], "The error message should specify the 'cep' field as problematic."
    assert 'CEP Não Encontrado' in body['detail'][0]['msg'], "The error message should clearly state that the CEP was not found."    
"""