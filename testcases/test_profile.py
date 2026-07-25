import pytest
import requests
from common.http_util import send_request


def test_token(acc_token):
    """使用 acc_token 调用个人信息接口，验证能成功返回个人信息。"""
    #headers={"Authorization": f"Bearer {acc_token}"}
    url = "https://api.escuelajs.co/api/v1/auth/profile"
    response=send_request(method="get",url=url)
    assert response.status_code==200