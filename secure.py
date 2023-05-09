from argon2 import PasswordHasher
import argon2
import jwt as pyjwt
from pydantic import BaseModel
from datetime import datetime, timedelta
from fastapi import FastAPI, Depends, HTTPException, Header
import os

class TokenData(BaseModel):
    sub: str

SECRET_KEY = os.environ['JWT_SECRET_KEY']

def generate_token(username: str) -> str:
    payload = {"sub": username}
    token = pyjwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_jwt_token(authorization: str = Header(...)) -> TokenData:
    try:
        token = authorization.split(" ")[1]
        payload = pyjwt.decode(token, SECRET_KEY, algorithms="HS256")
        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid JWT token")

        return TokenData(sub=user_id)

    except Exception as exception:
        print(exception)
        raise exception

def hash_pwd(pwd: str) -> str:
    ph = PasswordHasher()
    return ph.hash(pwd)

def verify_pwd(user_pwd: str, hashed_pwd: str) -> bool:
    ph = PasswordHasher()
    try:
        ph.verify(hashed_pwd, user_pwd)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False
