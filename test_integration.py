import pytest
import httpx
from api import api

def test_call_external_api():
    endpoint = "https://615f5fb4f7254d0017068109.mockapi.io/api/v1/cutomers"  # Utilisez un endpoint valide pour les tests
    response = api(endpoint)

    assert response.status_code == 200
    assert "data" in response.json()
