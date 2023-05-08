from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
import secure
import jwt
import requests
from secure import TokenData




app = FastAPI()
security = HTTPBearer()

# Vos informations d'identification d'utilisateur, stockées dans un dictionnaire

def api(url_api,way):

  req = requests.get(f'{url_api}{way}')
  wb = req.json()
  return wb




# Endpoint protégé par un jeton
@app.get("/customers")
async def protected_data_customers(token_data: TokenData = Depends(secure.verify_jwt_token)):

        # Renvoyer les données protégées

        return {"data": "Ceci sont des données protégées!"},api('https://615f5fb4f7254d0017068109.mockapi.io/api/v1','/customers')


@app.get("/orders")
async def protected_data_orders(id:str, token_data: TokenData = Depends(secure.verify_jwt_token)):

        # Renvoyer les données protégées

      try :

        return {"data": f"Ceci sont des données protégées!"},api('https://615f5fb4f7254d0017068109.mockapi.io/api/v1',f'/customers/{id}/orders')

      except :

        return {"data": "custumer_id do not exists !"}



@app.get("/products")
async def protected_data_products(customer_id:str, order_id:str,token_data: TokenData = Depends(secure.verify_jwt_token)):

        # Renvoyer les données protégées

      try :

        return {"data": f"Ceci sont des données protégées!"},api('https://615f5fb4f7254d0017068109.mockapi.io/api/v1',f'/customers/{customer_id}/orders/{order_id}/products')

      except :

        return {"data": "custumer_id or order_id do not exists !"}
