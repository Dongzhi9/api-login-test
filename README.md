# API Login Test

基于 **Python + Pytest + Requests** 实现的接口自动化测试框架。

支持接口请求封装、参数化、fixture 管理、日志记录、测试报告生成、数据库校验。

## 功能

- 登录接口测试（获取 token）
- 个人资料接口测试（携带 token 请求）
- 商品 CRUD 测试（创建/查询/修改/删除）
- 完整业务链路测试（创建 → 查询 → 修改 → 删除）
- 数据库数据校验（PyMySQL）
- 统一请求封装，自动打印请求/响应日志
- 配置与代码分离（多环境 YAML 配置）
- 全局 session 管理，token 自动注入请求头
- 失败自动重试（tenacity）
- 测试报告生成（pytest-html + Allure）

## 技术栈

| 技术 | 用途 |
|------|------|
| Python | 编程语言 |
| Pytest | 测试框架 |
| Requests | HTTP 请求 |
| Allure | 测试报告 |
| PyMySQL | 数据库校验 |
| Logging | 日志系统 |
| PyYAML | 配置管理 |
| Tenacity | 重试机制 |

## 项目结构

```
api-login-test/
├── common/                  # 公共工具
│   ├── __init__.py
│   ├── http_util.py         # 请求封装（session、timeout、retry、异常处理）
│   ├── mysql_util.py        # 数据库工具（连接、查询）
│   ├── logger_util.py       # 日志配置
│   ├── assert_util.py       # 统一断言
│   ├── response_util.py     # 响应 JSON 处理
│   ├── config_util.py       # YAML 配置读取
│   ├── config.py            # 全局配置入口
│   └── request_util.py      # 登录相关 fixture
├── config/                  # 环境配置
│   └── config.yaml          # 多环境 base_url、登录账号、MySQL
├── data/                    # 测试数据
│   └── product.yaml         # 商品参数化数据
├── testcases/               # 测试用例
│   ├── __init__.py
│   ├── conftest.py          # 全局 fixture（token、商品数据）
│   ├── test_login.py        # 登录测试
│   ├── test_profile.py      # 个人信息测试
│   ├── test_product.py      # 商品 CRUD 测试
│   └── test_mysql.py        # 数据库校验测试
├── logs/                    # 运行日志
├── reports/                 # 测试报告
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置

编辑 `config/config.yaml`：

```yaml
env: test

base_url:
  test: https://api.escuelajs.co/api/v1
  dev: https://dev-api.xxx.com
  prod: https://prod-api.xxx.com

login:
  email: john@mail.com
  password: changeme

mysql:
  host: 127.0.0.1
  port: 3306
  user: root
  password: "123456"
  database: test
```

切换环境只需修改 `env` 字段，无需改动代码。

### 3. 运行测试

```bash
# 运行所有测试
pytest

# 运行单个测试文件
pytest testcases/test_product.py -v

# 按标签运行
pytest -m smoke
```

### 4. 生成 Allure 报告

```bash
# 生成测试结果数据
pytest --alluredir=reports/result --clean-alluredir

# 查看报告
allure serve reports/result
```

### 5. 查看日志

运行结束后，日志记录在 `logs/test.log`。

## 设计说明

| 分层 | 职责 |
|------|------|
| `config/` | 环境配置，与代码分离 |
| `common/` | 工具封装（请求、数据库、日志、断言、配置） |
| `testcases/` | 测试用例，只关注业务逻辑 |

## 依赖

- Python 3.10+
- pytest
- requests
- allure-pytest
- pytest-html
- PyMySQL
- PyYAML
- tenacity
