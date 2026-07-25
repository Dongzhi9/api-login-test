import yaml
import os

def load_config():
    """从 config/config.yaml 加载配置，返回配置字典。"""
    path=os.path.join("config","config.yaml")
    with open(path,encoding="utf-8") as f:
        config=yaml.safe_load(f)
    return config