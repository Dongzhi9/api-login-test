import pytest
from common.request_util import token


def test_login(token):
    """验证能成功获取 access_token，不为 None。"""
    print(token)
    assert token is not None