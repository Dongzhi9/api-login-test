# API Login Test

Python + Requests + Pytest 接口自动化测试入门项目。

## 功能

- 登录接口测试（获取 token）
- 个人资料接口测试（携带 token 请求）
- 统一请求封装，自动打印请求/响应日志
- 配置与代码分离（YAML 配置）
- 全局 session 管理，token 自动注入请求头

## 项目结构

```
api-login-test/
├── config/
│   └── config.yaml          # 环境配置（URL、账号密码）
├── common/
│   ├── __init__.py
│   ├── config_util.py       # 配置加载工具
│   ├── http_util.py         # 统一 HTTP 请求封装
│   └── request_util.py      # 登录相关 fixture
├── testcases/
│   ├── __init__.py
│   ├── conftest.py          # 全局 fixture（token 注入）
│   ├── test_login.py        # 登录接口测试
│   └── test_profile.py      # 个人信息接口测试
├── .gitignore
├── README.md
└── requirements.txt
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行测试

```bash
# 运行所有测试
pytest

# 运行单个测试文件
pytest testcases/test_login.py -v

# 显示打印信息
pytest -v -s
```

### 3. 配置

编辑 `config/config.yaml`：

```yaml
base_url: https://api.escuelajs.co/api/v1
email: john@mail.com
password: changeme
```

## 设计说明

| 分层 | 职责 |
|------|------|
| `config/` | 环境配置，与代码分离 |
| `common/` | 工具封装（请求、配置读取、fixture 定义） |
| `testcases/` | 测试用例，只关注业务逻辑 |

## 依赖

- Python 3.10+
- requests
- pytest
- PyYAML
