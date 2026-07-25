import pytest
from common.request_util import token
from common.http_util import set_token

@pytest.fixture(scope="session")
def acc_token(token):
    """获取 token 并自动注入全局 session 的请求头。依赖 token fixture。"""
    acc_token=token
    set_token(acc_token)
    return acc_token