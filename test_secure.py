from secure import generate_token, verify_jwt_token, hash_pwd, verify_pwd
import pytest

def test_generate_and_verify_token():
    username = "webshop"
    token = generate_token(username)

    # Utilisez verify_jwt_token pour vérifier le jeton généré
    token_data = verify_jwt_token(f"Bearer {token}")

    assert token_data.sub == username

def test_hash_and_verify_password():
    plain_password = "test_password"
    hashed_password = hash_pwd(plain_password)

    assert verify_pwd(plain_password, hashed_password)
    assert not verify_pwd("wrong_password", hashed_password)
