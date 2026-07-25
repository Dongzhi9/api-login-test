import requests

session = requests.session()

def send_request(method, url, json=None, headers=None):
    """统一发送 HTTP 请求，自动打印请求和响应的详细信息。"""
    print("="*30)
    print("request")
    print("method:",method)
    print("url:",url)
    print("json:",json)
    print("headers:",headers)

    response=session.request(
        method=method,
        url=url,
        json=json,
        headers=headers)

    print("="*30)
    print("response")
    print("Status code:",response.status_code)
    print("body:",response.text)

    return response

def set_token(token):
    """将 Bearer token 设置到全局 session 的请求头中，后续请求自动携带。"""
    session.headers.update({
        "Authorization": f"Bearer {token}"
    })