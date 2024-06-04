import httpx

async def validate_cep(value: str) -> dict:
    """
    Validates and fetches address data from a given CEP (Postal Code) using the ViaCEP API.

    Args:
        value (str): The CEP code to be validated.

    Returns:
        dict: A dictionary containing address data such as state, city, neighborhood, and road.

    Raises:
        ValueError: If the CEP code is not found or if there is a failure in accessing the CEP service.
    """
    url = f"https://viacep.com.br/ws/{value}/json/"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response_data = response.json()
            if 'erro' in response_data:
                raise ValueError("CEP Code Not Found")
        except httpx.RequestError:
            raise ValueError("Failed to access the CEP service")    
        
        return response_data