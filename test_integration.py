import pytest
import httpx
from api import api
from fastapi import HTTPException

def test_api_call_success_customers():
    endpoint = "/customers"  # Utilisez un endpoint valide pour les tests
    response_data = api(endpoint)

    assert response_data is not None
    assert isinstance(response_data, list)

def test_api_call_success_order():

    id = 8
    endpoint = "/orders?id={id}"  # Utilisez un endpoint valide pour les tests
    response_data = api(endpoint)

    assert response_data is not None
    assert isinstance(response_data, list)

def test_api_call_success_order():

    customer_id = 8
    order_id = 8
    endpoint = "/products?customer_id={customer_id}&order_id={order_id}"  # Utilisez un endpoint valide pour les tests
    response_data = api(endpoint)

    assert response_data is not None
    assert isinstance(response_data, list)

def test_api_call_failure():
    invalid_endpoint = "/invalid/endpoint"  # Utilisez un endpoint non valide pour les tests

    with pytest.raises(HTTPException) as exc_info:
        api(invalid_endpoint)

    assert exc_info.value.status_code == 500
