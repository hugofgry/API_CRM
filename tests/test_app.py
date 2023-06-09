import pytest
import httpx
import os

token = os.environ['TOK']


def base(env):

  if env=='github' :

    API_BASE_URL = "http://127.0.0.1:8080"

    return API_BASE_URL

  else :

    API_BASE_URL = "https://apiepsicrm.herokuapp.com"

    return API_BASE_URL

API_BASE_URL = base('github')

def test_customers():

    headers = {"Authorization": f"Bearer {token}"}
    response = httpx.get(f"{API_BASE_URL}/customers", headers=headers)
    assert response.status_code == 200

def test_orders():

    id = 8  # Un exemple d'ID valide
    headers = {"Authorization": f"Bearer {token}"}
    response = httpx.get(f"{API_BASE_URL}/orders?id={id}", headers=headers)
    assert response.status_code == 200

def test_products():

    customer_id = 8  # Un exemple d'ID de client valide
    order_id = 8  # Un exemple d'ID de commande valide
    headers = {"Authorization": f"Bearer {token}"}
    response = httpx.get(
        f"{API_BASE_URL}/products?customer_id={customer_id}&order_id={order_id}",
        headers=headers,
    )
    assert response.status_code == 200

def test_orders_invalid_customer_id():

    invalid_id = 9999  # Un exemple d'ID client invalide
    headers = {"Authorization": f"Bearer {token}"}
    response = httpx.get(f"{API_BASE_URL}/orders?id={invalid_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["data"] == "custumer_id do not exists !"

def test_products_invalid_ids():

    invalid_customer_id = 9999  # Un exemple d'ID client invalide
    invalid_order_id = 9999  # Un exemple d'ID commande invalide
    headers = {"Authorization": f"Bearer {token}"}
    response = httpx.get(
        f"{API_BASE_URL}/products?customer_id={invalid_customer_id}&order_id={invalid_order_id}",
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json()["data"] == "custumer_id or order_id do not exists !"

def test_invalid_token():

    invalid_token = "Bearer eyhbGciOiJIUzI1NiInR5I6IkpXVCJ9.eyJzdJ3ZWJ9wMQNBvnNXB_bD32fx8Bgimw0,k,jojUaBldDD2lGYQ"
    headers = {"Authorization": f"Bearer {invalid_token}"}

    response_customers = httpx.get(f"{API_BASE_URL}/customers", headers=headers)
    response_orders = httpx.get(f"{API_BASE_URL}/orders?id=1", headers=headers)
    response_products = httpx.get(f"{API_BASE_URL}/products?customer_id=1&order_id=1", headers=headers)

    assert response_customers.status_code == 401
    assert response_orders.status_code == 401
    assert response_products.status_code == 401


#HDHDCJd
