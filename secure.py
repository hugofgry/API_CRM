import argon2
import jwt as pyjwt
from pydantic import BaseModel
from datetime import datetime, timedelta
from fastapi import FastAPI, Depends, HTTPException, Header
import os


class TokenData(BaseModel):
  sub: str



# Clé secrète pour signer les jetons JWT
SECRET_KEY = os.env['JWT_SECRET_KEY']

# Durée de validité du jeton (nous utilisons timedelta pour que nous puissions facilement ajouter ou soustraire du temps)
TOKEN_EXPIRATION_TIME = timedelta(days=7)

def generate_token(username: str) -> str:
    # Définir la date d'expiration du jeton
    expiration = datetime.utcnow() + TOKEN_EXPIRATION_TIME

    # Créer la charge utile pour le jeton JWT (nous incluons le nom d'utilisateur et la date d'expiration)
    payload = {"sub": username, "exp": expiration}

    # Créer le jeton JWT en signant la charge utile avec la clé secrète
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    # Retourner le jeton en tant que chaîne de caractères
    return token

def verify_jwt_token(authorization: str = Header(...)) -> TokenData:

  try:

    token = authorization.split(" ")[1]
    payload = pyjwt.decode(token, SECRET_KEY, algorithms="HS256")
    # Reste de la fonction
    user_id = payload.get("sub")

    if user_id is None:

      raise HTTPException(status_code=401, detail="Invalid JWT token")

      token_data = TokenData(sub=user_id)

      return token_data

  except pyjwt.exceptions.ExpiredSignatureError:

    raise HTTPException(status_code=401, detail="JWT token has expired")

  except pyjwt.exceptions.InvalidSignatureError:

    raise HTTPException(status_code=401, detail="Invalid JWT signature")

  except pyjwt.PyJWTError:

    raise HTTPException(status_code=401, detail="Invalid JWT token")

def hash_pwd(pwd: str) -> str:
    ph = argon2.PasswordHasher()
    return ph.hash(pwd)


def verify_pwd(user_pwd: str, hashed_pwd: str) -> bool:
    hashed_user_password = hash_pwd(user_pwd)
    try:
        ph.verify(hashed_user_password, hashed_pwd)
        return True
    except:
        return False




