# redis
<!-- TOC -->
* [redis](#redis)
  * [安装](#安装)
  * [重启](#重启)
  * [远程权限](#远程权限)
<!-- TOC -->
## 安装

```shell
curl -OJL https://github.com/redis/redis/archive/7.0.11.tar.gz
tar -zxvf redis-7.0.11.tar.gz
cd redis-7.0.11
make
make install
redis-server
```

## 重启

```shell
service redis-server restart
```

## 远程权限

1. 打开服务商安全组端口
2. 打开系统防火墙端口
3. 修改redis.conf的bind-address为0.0.0.0
4. 重启redis
