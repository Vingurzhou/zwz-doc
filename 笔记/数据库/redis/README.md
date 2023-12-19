# redis

<!-- TOC -->

* [redis](#redis)
    * [重启](#重启)
    * [远程权限](#远程权限)

<!-- TOC -->

## 重启

```shell
service redis-server restart
```

## 远程权限

1. 打开服务商安全组端口
2. 打开系统防火墙端口
3. 修改redis.conf的bind-address为0.0.0.0
4. 重启redis

## msgpack

```python
import redis
import msgpack
import json

# 连接到Redis
redis_host = 'localhost'
redis_port = 10265
redis_password = 'enjoy:Yuhu8888'
redis_db = 0

# 创建Redis连接对象
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, db=redis_db)

# 获取数据
key = '4f86947b6d39afca04654b0145daea31'
packed_data = redis_client.get(key)

if packed_data:
    # 解码msgpack数据
    unpacked_data = msgpack.unpackb(packed_data, raw=False)

    # 打印序列化前的JSON
    json_data = json.dumps(unpacked_data, indent=2, ensure_ascii=False)
    print(json_data)
else:
    print(f"Key '{key}' not found in Redis.")

```

## 扩容机制