import requests
import pytest
from common.http_util import send_request
from common.config_util import load_config

@pytest.fixture(scope="session")
def token():
    config=load_config()
    url=config["base_url"]+ "/auth/login"
    payload={
        "email": config["email"],
        "password": config["password"]
        }
    response=send_request(method="POST",url=url,json=payload)
    data=response.json()
    assert response.status_code==201
    assert "access_token" in data
    token=data["access_token"]
    return token


