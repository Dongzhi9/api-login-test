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
def update_product_payload():

    payload ={
        "title": f"test_product{int(time.time()*1000)}",
        "price": 100,
        "description": "string",
        "categoryId": 1,
        "images": [
            "https://placehold.co/600x400"
        ]
    }
    return payload

@pytest.fixture
def create_product(update_product_payload):

    url = "https://api.escuelajs.co/api/v1/products"

    response = send_request(
        method="post",
        url=url,
        json=update_product_payload
    )
    data = response.json()
    if response.status_code != 201:
        raise RuntimeError(f"创建测试商品失败:{response.text}")

    yield  data["id"]

    response_del=send_request(
        method="delete",
        url=f"{url}/{data['id']}"
    )

    if response_del.status_code == 200:
        print("测试清理：删除成功")
    elif response_del.status_code == 400:
        print("测试清理：商品不存在")
    else:
        raise RuntimeError(
            f"清理失败:{response_del.text}"
        )
