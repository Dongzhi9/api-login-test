import time
import pytest
from common.http_util import send_request
from common.config_util import load_product
from common.config_util import load_config

BASE_URL = load_config()["base_url"]
 
def test_get_products():

    url = f"{BASE_URL}/products"

    response = send_request(
                method="get",
                url=url
            )

    data = response.json()
    print(data)
    assert response.status_code == 200
    assert isinstance(data,list)
    assert len(data)>0

product_data = load_product()["product"]
@pytest.mark.parametrize(
    "product",
    product_data
)
def test_create_product(product):

    url = f"{BASE_URL}/products"

    payload = {
        "title": f"{product['title']}_{int(time.time()*10)}",
        "price": product["price"],
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

    url = f"{BASE_URL}/products/{create_product}"

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

    url = f"{BASE_URL}/products/{create_product}"

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

    url = f"{BASE_URL}/products/{create_product}"

    response = send_request(
        method="delete",
        url=url
    )
    print(response.text)
    assert response.status_code == 200

def test_product_full_business_flow(create_product):
    """完整业务链路：创建 → 查询 → 修改 → 删除"""
    base_url = f"{BASE_URL}/products"

    res_get = send_request("get", f"{base_url}/{create_product}")
    assert res_get.status_code == 200
    assert res_get.json()["id"] == create_product

    update_payload = {
        "title":"flow_updated",
        "price":200,
        "description":"update",
        "categoryId":1,
        "images":["https://placehold.co/600x400"]
    }
    res_update = send_request("put", f"{base_url}/{create_product}", json=update_payload)
    assert res_update.status_code == 200
    assert res_update.json()["title"] == update_payload["title"]

    res_del = send_request("delete", f"{base_url}/{create_product}")
    assert res_del.status_code == 200