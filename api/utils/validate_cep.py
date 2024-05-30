import httpx

def validate_cep(value):
    url = f"https://viacep.com.br/ws/{value}/json/"
    try:
        response = httpx.get(url)
        response_data = response.json()
        if 'erro' in response_data:
            raise ValueError("CEP Não Encontrado")
    except httpx.RequestError:
        raise ValueError("Falha ao acessar o serviço de CEP")    
    
    return response_data