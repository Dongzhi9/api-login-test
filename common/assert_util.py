def assert_status_code(response,expected_code):
    assert response.status_code == expected_code,\
         f"状态码不符: 期望{expected_code}, 实际{response.status_code}, body:{response.text}"

def assert_json_key(data,key):
    assert key in data,f"响应缺少字段:{key}"
    
def assert_json_value(data,key,value):
    assert data[key] == value, \
        f"{key}实际:{data[key]},期望:{value}"