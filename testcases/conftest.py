import pytest
from common.request_util import token

@pytest.fixture(scope="session")
def acc_token(token):
    acc_token=token
    return acc_token