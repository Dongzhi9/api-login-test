import pymysql
from common.config_util import load_config

def get_connection():
    config = load_config()["mysql"]
    host = config["host"]
    port = config["port"]
    user = config["user"]
    password = config["password"]
    database = config["database"]
    con = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        charset="utf8"
    )
    return con

def query_one(sql):
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

