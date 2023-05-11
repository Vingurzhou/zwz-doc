# python

<!-- TOC -->
* [python](#python)
  * [生成依赖](#生成依赖)
  * [安装依赖](#安装依赖)
  * [找不到库](#找不到库)
<!-- TOC -->

## 生成依赖

```shell
pip freeze > requirements.txt
```

## 安装依赖

```shell
pip install -r requirements.txt

```

## 找不到库

```python
import sys

sys.path.append('/path/to/PIL')
```
##  urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with LibreSSL 2.8.3.
```shell
pip3 install "urllib3 <=1.26.15"

```