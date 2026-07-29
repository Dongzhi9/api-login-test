import requests
import pytest
from common.http_util import send_request
from common.config import LOGIN_EMAIL,LOGIN_PASSWORD,BASE_URL
from common.response_util import get_json

@pytest.fixture(scope="session")
def token():
    """登录获取 access_token，整个测试会话只执行一次。"""
    url=BASE_URL+ "/auth/login"
    payload={
        "email": LOGIN_EMAIL,
        "password": LOGIN_PASSWORD
        }
    response=send_request(method="POST",url=url,json=payload)
    data=get_json(response)
    assert response.status_code==201
    assert "access_token" in data
    token=data["access_token"]
    return token


