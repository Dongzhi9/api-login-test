import logging
import os

def setup_logger():
    """配置日志器，输出到控制台和文件"""
    logger = logging.getLogger("api_test")
    logger.setLevel(logging.DEBUG)

    # 控制台 handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 文件 handler
    os.makedirs("logs", exist_ok=True)
    file_handler = logging.FileHandler(
        os.path.join("logs", "test.log"), encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)

    # 格式
    formatter = logging.Formatter(
        "%(asctime)s  %(levelname)s  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


logger = setup_logger()