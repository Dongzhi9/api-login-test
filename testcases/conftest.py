import pytest
import time
from common.request_util import token
from common.http_util import set_token
from common.http_util import send_request

@pytest.fixture(scope="session")
def acc_token(token):
    """获取 token 并自动注入全局 session 的请求头。依赖 token fixture。"""
    acc_token=token
    set_token(acc_token)
    return acc_token

@pytest.fixture
def create_product():

    url = "https://api.escuelajs.co/api/v1/products"

    payload ={
        "title": f"test_product{int(time.time()*1000)}",
        "price": 100,
        "description": "string",
        "categoryId": 1,
        "images": [
            "https://placehold.co/600x400"
        ]
    }
    response = send_request(
        method="post",
        url=url,
        json=payload
    )
    data = response.json()
    assert response.status_code == 201
    return data["id"]