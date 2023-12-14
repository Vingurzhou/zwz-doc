# python

<!-- TOC -->

* [python](#python)
    * [术语](#术语)
    * [环境依赖管理](#环境依赖管理)
        * [虚拟环境](#虚拟环境)
        * [生成依赖](#生成依赖)
        * [安装依赖](#安装依赖)
        * [找不到库](#找不到库)
    * [其他](#其他)
        * [urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with LibreSSL 2.8.3.](#urllib3-v20-only-supports-openssl-111-currently-the--ssl-module-is-compiled-with-libressl-283)

<!-- TOC -->

## 术语

| 简称   | 全称                                  | 含义         |
|------|-------------------------------------|------------|
| OOP  | Object-Oriented Programming         | 面向对象编程     |
| OOAD | Object-Oriented Analysis and Design | 面向对象的分析和设计 |
| DDD  | Domain-Driven Design                | 领域驱动设计     |

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

## re

```python
pattern = re.compile(
    r"""<th class=".*?">.*?<a href="(.*?)" onclick="atarget(this)" class="xst" >(.*?)</a>.*?</th>""", re.S)
print(pattern)
re.findall(pattern, text, )
```

## soup

```python
    threads1 = soup.find_all('th', class_='common')
    threads2 = soup.find_all('th', class_='lock')
    threads=threads1+threads2
    for thread in threads:
        category = thread.find_all('a')[0].text.strip()
        title = thread.find_all('a')[0].text.strip()
        content = thread.find_all('a', class_='xst')[0].text.strip()
        author = thread.find_next_sibling('td', class_='by').cite.a.text.strip()
        date = thread.find_next_sibling('td', class_='by').em.span.text.strip()

        print(i[0], category, title, author, content, date)
```

### 替换

```python
pattern = re.compile(r'<.*?>|&nbsp;')
# 使用正则表达式去除HTML标签
s = re.sub(pattern, '', match)

```

## 其他

### urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with LibreSSL 2.8.3.

```shell
pip3 install "urllib3 <=1.26.15"

```
