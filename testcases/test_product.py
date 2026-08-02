import time
import pytest
import allure
from common.http_util import send_request
from common.config_util import load_product
from common.config import BASE_URL
from common.assert_util import assert_status_code,assert_json_key,assert_json_value
from common.response_util import get_json
 
def test_get_products():

    url = f"{BASE_URL}/products"

    response = send_request(
                method="get",
                url=url
            )

    data = get_json(response)
    assert_status_code(response,200)
    assert isinstance(data,list)
    assert len(data)>0

product_data = load_product()["product"]
@allure.story("创建商品")
@allure.title("创建商品接口")
@pytest.mark.parametrize(
    "product",
    product_data
)
@allure.feature("商品管理")
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
    data = get_json(response)
    assert_status_code(response,201)
    assert_json_key(data,"id")

def test_get_product_detail(create_product):

    url = f"{BASE_URL}/products/{create_product}"

    response = send_request(
                method="get",
                url=url
            )

    data = get_json(response)
    assert_status_code(response,200)
    assert_json_value(data,"id",create_product)
    assert isinstance(data,dict)

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
    data = get_json(response)
    assert_status_code(response,200)
    assert_json_value(data,"title",payload["title"])

def test_delete_product(create_product):

    url = f"{BASE_URL}/products/{create_product}"

    response = send_request(
        method="delete",
        url=url
    )
    assert_status_code(response,200)

@allure.feature("商品管理")
@allure.story("完整业务流程")
@allure.title("创建→查询→修改→删除")
def test_product_full_business_flow(create_product):
    """完整业务链路：创建 → 查询 → 修改 → 删除"""
    base_url = f"{BASE_URL}/products"

    res_get = send_request("get", f"{base_url}/{create_product}")
    assert_status_code(res_get,200)
    data_get = get_json(res_get)
    assert_json_value(data_get,"id",create_product)

    update_payload = {
        "title":"flow_updated",
        "price":200,
        "description":"update",
        "categoryId":1,
        "images":["https://placehold.co/600x400"]
    }
    res_update = send_request("put", f"{base_url}/{create_product}", json=update_payload)
    assert_status_code(res_update,200)
    data_update = get_json(res_update)
    assert_json_value(data_update,"title",update_payload["title"])

    res_del = send_request("delete", f"{base_url}/{create_product}")
    assert_status_code(res_del,200)