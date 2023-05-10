import pytest
import httpx
from api import api

def test_call_external_api():
    endpoint = "/customers"  # Utilisez un endpoint valide pour les tests
    response = api(endpoint)

    assert response == 200
    assert "data" in response
