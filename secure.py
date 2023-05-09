import argon2
import jwt as pyjwt
from pydantic import BaseModel
from datetime import datetime, timedelta
from fastapi import FastAPI, Depends, HTTPException, Header
import os


class TokenData(BaseModel):
  sub: str





# Clé secrète pour signer les jetons JWT
SECRET_KEY = os.environ['JWT_SECRET_KEY']




def generate_token(username: str) -> str:

    # Créer la charge utile pour le jeton JWT (nous incluons le nom d'utilisateur et la date d'expiration)
    payload = {"sub": username}

    # Créer le jeton JWT en signant la charge utile avec la clé secrète
    token = pyjwt.encode(payload, SECRET_KEY, algorithm="HS256")

    # Retourner le jeton en tant que chaîne de caractères
    return token

def verify_jwt_token(authorization: str = Header(...)) -> TokenData:
  print(authorization)


  try:

    token = authorization.split(" ")[1]
    payload = pyjwt.decode(token, SECRET_KEY, algorithms="HS256")
    # Reste de la fonction
    user_id = payload.get("sub")

    if user_id is None:

        raise HTTPException(status_code=401, detail="Invalid JWT token")

    token_data = TokenData(sub=user_id)

    return token_data

  except:

    raise HTTPException(status_code=401, detail="Invalid JWT token")

def hash_pwd(pwd: str) -> str:
    ph = argon2.PasswordHasher()
    return ph.hash(pwd)


def verify_pwd(user_pwd: str, hashed_pwd: str) -> bool:
    ph = argon2.PasswordHasher()

    try:
        ph.verify(hashed_pwd, user_pwd)
        return True
    except:
        return False



