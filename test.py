import pytest
import httpx

API_BASE_URL = "https://your-heroku-app.herokuapp.com"  # Remplacez par l'URL de votre application Heroku

def test_customers(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = httpx.get(f"{API_BASE_URL}/customers", headers=headers)
    assert response.status_code == 200

def test_orders(token):
    id = 1  # Un exemple d'ID valide
    headers = {"Authorization": f"Bearer {token}"}
    response = httpx.get(f"{API_BASE_URL}/orders?id={id}", headers=headers)
    assert response.status_code == 200

def test_products(token):
    customer_id = 1  # Un exemple d'ID de client valide
    order_id = 1  # Un exemple d'ID de commande valide
    headers = {"Authorization": f"Bearer {token}"}
    response = httpx.get(
        f"{API_BASE_URL}/products?customer_id={customer_id}&order_id={order_id}",
        headers=headers,
    )
    assert response.status_code == 200
