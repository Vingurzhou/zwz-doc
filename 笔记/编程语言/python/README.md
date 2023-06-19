# python

<!-- TOC -->
* [python](#python)
  * [环境依赖管理](#环境依赖管理)
    * [虚拟环境](#虚拟环境)
    * [生成依赖](#生成依赖)
    * [安装依赖](#安装依赖)
    * [找不到库](#找不到库)
  * [其他](#其他)
    * [urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with LibreSSL 2.8.3.](#urllib3-v20-only-supports-openssl-111-currently-the--ssl-module-is-compiled-with-libressl-283)
<!-- TOC -->

## 环境依赖管理

### 虚拟环境

```shell
python3 -m venv env
source env/bin/activate
deactivate
```

### 生成依赖

```shell
pip freeze > requirements.txt
```

### 安装依赖

```shell
pip install -r requirements.txt

```

### 找不到库

```python
import sys

sys.path.append('/path/to/PIL')
```

## 其他

### urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with LibreSSL 2.8.3.

```shell
pip3 install "urllib3 <=1.26.15"

```
