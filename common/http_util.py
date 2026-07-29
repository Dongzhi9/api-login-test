import requests
from tenacity import retry, stop_after_attempt, wait_fixed

session = requests.session()

def print_request(method, url, json):
    print("="*30)
    print("request")
    print("method:",method)
    print("url:",url)
    print("json:",json)
    print("headers:",session.headers)

def print_response(response):
    print("="*30)
    print("response")
    print("Status code:",response.status_code)
    print("body:",response.text)

@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def send_request(method, url, json=None, headers=None):
    """统一发送 HTTP 请求，自动打印请求和响应的详细信息。"""

    print_request(method, url, json)

    try:
        response=session.request(
            method=method,
            url=url,
            json=json,
            headers=headers,
            timeout=10
        )
    except requests.exceptions.Timeout:
        raise RuntimeError(f"请求超时:{method} {url}")
    except requests.exceptions.ConnectionError:
        raise RuntimeError(f"网络连接失败:{method} {url}")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"请求异常:{e}")

    print_response(response)

    if response.status_code in [502,503,504]:
        raise RuntimeError(
            f"服务器临时错误:{response.status_code}"
        )
    
    return response

def set_token(token):
    """将 Bearer token 设置到全局 session 的请求头中，后续请求自动携带。"""
    session.headers.update({
        "Authorization": f"Bearer {token}"
    })