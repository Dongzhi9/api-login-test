import pytest
from common.request_util import token


@pytest.mark.smoke
def test_login(token):
    """验证能成功获取 access_token,不为 None。"""
    assert token is not None
    print("token获取成功")