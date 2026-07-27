import yaml
import os

def load_config():
    path = os.path.join("config","config.yaml")
    with open(path,encoding="utf-8") as f:
        config=yaml.safe_load(f)
    return config

def load_product():
    path = os.path.join("data","product.yaml")
    with open(path,encoding="utf-8") as f:
        product=yaml.safe_load(f)
    return product