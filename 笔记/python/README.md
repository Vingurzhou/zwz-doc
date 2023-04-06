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