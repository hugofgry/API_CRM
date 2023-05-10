import os
import sys
parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))

# ajouter le chemin absolu du répertoire parent au chemin de recherche Python
sys.path.append(parent_dir)


from secure import generate_token, verify_jwt_token, hash_pwd, verify_pwd
import pytest

def test_generate_and_verify_token():
    username = "webshop"
    token = generate_token(username)

    # Utilisez verify_jwt_token pour vérifier le jeton généré
    token_data = verify_jwt_token(f"Bearer {token}")

    assert token_data.sub == username
#A
