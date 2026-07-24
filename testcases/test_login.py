import pytest
from common.request_util import token

def test_login(token):
    print(token)
    assert token is not None