from common.config_util import load_config

config = load_config()
BASE_URL = config["base_url"][config["env"]]
LOGIN_EMAIL = config["login"]["email"]
LOGIN_PASSWORD = config["login"]["password"]