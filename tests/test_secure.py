import os
import sys
script_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


sys.path.insert(0, script_path)



from secure import generate_token, verify_jwt_token, hash_pwd, verify_pwd
import pytest

def test_generate_and_verify_token():
    username = "webshop"
    token = generate_token(username)


    token_data = verify_jwt_token(f"Bearer {token}")

    assert token_data.sub == username
#A
