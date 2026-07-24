import requests
import pytest
from common.http_util import send_request

@pytest.fixture(scope="session")
def token():
    url="https://api.escuelajs.co/api/v1/auth/login"
    payload={
    "email": "john@mail.com",
    "password": "changeme"
    }
    response=send_request(method="POST",url=url,json=payload)
    data=response.json()
    assert response.status_code==201
    assert "access_token" in data
    token=data["access_token"]
    return token


