import pytest
import requests
from common.http_util import send_request
from common.config_util import load_config

BASE_URL = load_config()["base_url"]

def test_token(acc_token):
    """使用 acc_token 调用个人信息接口，验证能成功返回个人信息。"""
    #headers={"Authorization": f"Bearer {acc_token}"}
    url = f"{BASE_URL}/auth/profile"
    response=send_request(method="get",url=url)
    assert response.status_code==200