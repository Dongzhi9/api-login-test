import time
import pytest
from common.http_util import send_request

def test_get_products():

    url = "https://api.escuelajs.co/api/v1/products"

    response = send_request(
                method="get",
                url=url
            )

    data = response.json()
    print(data)
    assert response.status_code == 200
    assert isinstance(data,list)
    assert len(data)>0

@pytest.mark.parametrize("title,price",
    [('phone',1000),
     ('laptop',500),
     ('book',50)
])
def test_create_product(title,price):

    url = "https://api.escuelajs.co/api/v1/products"

    payload = {
        "title": f"{title}_{int(time.time()*10)}",
        "price": price,
        "description": "string",
        "categoryId": 1,
        "images": [
            "https://placehold.co/600x400"
        ]
    }
    response = send_request(
        method="post",
        url=url,
        json=payload
    )
    data = response.json()
    print(data)
    assert response.status_code == 201
    assert "id" in data

def test_get_product_detail(create_product):

    url = f"https://api.escuelajs.co/api/v1/products/{create_product}"

    response = send_request(
                method="get",
                url=url
            )

    data = response.json()
    print(data)
    assert response.status_code == 200
    assert isinstance(data,dict)
    assert data["id"] == create_product

def test_update_product(create_product):

    url = f"https://api.escuelajs.co/api/v1/products/{create_product}"

    payload = {
        "title": f"updated_product{int(time.time()*10)}",
        "price": 200,
        "description": "updated description",
        "categoryId": 1,
        "images": [
            "https://placehold.co/600x400"
        ]
    }
    response = send_request(
        method="put",
        url=url,
        json=payload
    )
    data = response.json()
    print(data)
    assert response.status_code == 200
    assert data["title"] == payload["title"]

def test_delete_product(create_product):

    url = f"https://api.escuelajs.co/api/v1/products/{create_product}"

    response = send_request(
        method="delete",
        url=url
    )
    print(response.text)
    assert response.status_code == 200