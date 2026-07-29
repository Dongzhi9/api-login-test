def get_json(response):
    """安全获取响应 JSON，解析失败时抛出明确错误。"""
    try:
        return response.json()
    except Exception:
        raise RuntimeError(f"响应不是合法JSON:{response.text[:200]}")