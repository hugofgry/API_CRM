from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import secure
import requests
from secure import TokenData


app = FastAPI()
security = HTTPBearer()


def api(endpoint: str) -> dict:
    base_url = "https://615f5fb4f7254d0017068109.mockapi.io/api/v1"
    try:
        response = requests.get(f"{base_url}{endpoint}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/customers")
async def protected_data_customers(token_data: TokenData = Depends(secure.verify_jwt_token)):
    return {"data": "Ceci sont des données protégées!"}, api("/customers")


@app.get("/orders")
async def protected_data_orders(id: str, token_data: TokenData = Depends(secure.verify_jwt_token)):
    try:
        return {"data": f"Ceci sont des données protégées!"}, api(f"/customers/{id}/orders")
    except HTTPException as e:
        return {"data": "custumer_id do not exists !"}


@app.get("/products")
async def protected_data_products(customer_id: str, order_id: str, token_data: TokenData = Depends(secure.verify_jwt_token)):
    try:
        return {"data": f"Ceci sont des données protégées!"}, api(f"/customers/{customer_id}/orders/{order_id}/products")
    except HTTPException as e:
        return {"data": "custumer_id or order_id do not exists !"}

@app.get("/fgg")
async def protected_data_products():
  print('hello')
