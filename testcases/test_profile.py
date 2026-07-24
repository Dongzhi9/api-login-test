import pytest
import requests
from common.http_util import send_request 
def test_token(acc_token):
    headers={
        "Authorization": f"Bearer {acc_token}"
    }
    url = "https://api.escuelajs.co/api/v1/auth/profile"
    response=send_request(method="get",url=url,headers=headers)
    assert response.status_code==200