import pytest
from common.request_util import token
from common.http_util import set_token

@pytest.fixture(scope="session")
def acc_token(token):
    acc_token=token
    set_token(acc_token)
    return acc_token