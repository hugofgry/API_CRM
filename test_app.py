import pytest
import httpx

API_BASE_URL = "https://apiepsicrm.herokuapp.com"

def test_customers():
    headers = {"Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3ZWJzaG9wIn0.FJQHrzjTKvTEBkiHRQgHzv1-BVzH1IkcYp8YHmJs1hA"}
    response = httpx.get(f"{API_BASE_URL}/customers", headers=headers)
    assert response.status_code == 200

def test_orders():
    id = 8  # Un exemple d'ID valide
    headers = {"Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3ZWJzaG9wIn0.FJQHrzjTKvTEBkiHRQgHzv1-BVzH1IkcYp8YHmJs1hA"}
    response = httpx.get(f"{API_BASE_URL}/orders?id={id}", headers=headers)
    assert response.status_code == 200

def test_products():
    customer_id = 8  # Un exemple d'ID de client valide
    order_id = 8  # Un exemple d'ID de commande valide
    headers = {"Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3ZWJzaG9wIn0.FJQHrzjTKvTEBkiHRQgHzv1-BVzH1IkcYp8YHmJs1hA"}
    response = httpx.get(
        f"{API_BASE_URL}/products?customer_id={customer_id}&order_id={order_id}",
        headers=headers,
    )
    assert response.status_code == 200
