import requests

session = requests.session()

def send_request(method,url,json=None,headers=None):
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
    session.headers.update({
        "Authorization": f"Bearer {token}"
    })