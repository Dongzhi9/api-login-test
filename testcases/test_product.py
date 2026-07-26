from common.http_util import send_request

product_id=None

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

def test_create_product():

    global product_id

    url = "https://api.escuelajs.co/api/v1/products"

    payload = {
        "title": "string_4",
        "price": 100,
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
    product_id = data["id"]
    print("创建商品id:", product_id)

def test_get_product_detail():

    url = f"https://api.escuelajs.co/api/v1/products/{product_id}"

    response = send_request(
                method="get",
                url=url
            )

    data = response.json()
    print(data)
    assert response.status_code == 200
    assert isinstance(data,dict)
    assert data["id"] == product_id

def test_update_product():

    url = f"https://api.escuelajs.co/api/v1/products/{product_id}"

    payload = {
        "title": "updated_product_2",
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
    assert data["title"] == "updated_product_2"

def test_delete_product():

    url = f"https://api.escuelajs.co/api/v1/products/{product_id}"

    response = send_request(
        method="delete",
        url=url
    )
    print(response.text)
    assert response.status_code == 200