import pytest
import httpx
from api import api

def test_call_external_api():
    endpoint = "/cutomers/"  # Utilisez un endpoint valide pour les tests
    response = api(endpoint)

    assert response.status_code == 200
    assert "data" in response.json()
