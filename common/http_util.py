import requests
from common.logger_util import logger
from tenacity import retry, stop_after_attempt, wait_fixed

session = requests.session()

def log_request(method, url, json):
    logger.info("="*30)
    logger.info("request")
    logger.info(f"method:{method}")
    logger.info(f"url:{url}")
    logger.info(f"json:{json}")
    logger.info(f"headers:{session.headers}")

def log_response(response):
    logger.info("="*30)
    logger.info("response")
    logger.info(f"Status code:{response.status_code}")
    logger.info(f"body:{response.text}")

@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def send_request(method, url, json=None, headers=None):
    """统一发送 HTTP 请求，自动打印请求和响应的详细信息。"""

    log_request(method, url, json)

    try:
        response=session.request(
            method=method,
            url=url,
            json=json,
            headers=headers,
            timeout=10
        )
    except requests.exceptions.Timeout:
        logger.error(f"请求超时:{method} {url}")
        raise RuntimeError(f"请求超时:{method} {url}")
    except requests.exceptions.ConnectionError:
        logger.error(f"网络连接失败:{method} {url}")
        raise RuntimeError(f"网络连接失败:{method} {url}")
    except requests.exceptions.RequestException as e:
        logger.error(f"请求异常:{e}")
        raise RuntimeError(f"请求异常:{e}")

    log_response(response)

    if response.status_code in [502,503,504]:
        logger.warning(f"服务器临时错误:{response.status_code},准备重试")
        raise RuntimeError(
            f"服务器临时错误:{response.status_code}"
        )
    
    return response

def set_token(token):
    """将 Bearer token 设置到全局 session 的请求头中，后续请求自动携带。"""
    session.headers.update({
        "Authorization": f"Bearer {token}"
    })