import pytest
import httpx
from fastapi import HTTPException
import os
import sys
script_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ajouter le chemin absolu à sys.path
sys.path.insert(0, script_path)

from api import api


def test_api_call_success_customers():
    endpoint = "/customers"  # Utilisez un endpoint valide pour les tests
    response_data = api(endpoint)

    assert response_data is not None
    assert isinstance(response_data, list)

def test_api_call_success_order():

    endpoint = "/customers/8/orders/"  # Utilisez un endpoint valide pour les tests
    response_data = api(endpoint)

    assert response_data is not None
    assert isinstance(response_data, list)

def test_api_call_success_product():


    endpoint = f"/customers/8/orders/8/products"  # Utilisez un endpoint valide pour les tests
    response_data = api(endpoint)

    assert response_data is not None
    assert isinstance(response_data, list)

def test_api_call_failure():
    invalid_endpoint = "/invalid/endpoint"  # Utilisez un endpoint non valide pour les tests

    with pytest.raises(HTTPException) as exc_info:
        api(invalid_endpoint)

    assert exc_info.value.status_code == 500
