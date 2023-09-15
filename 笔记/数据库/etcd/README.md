# etcd

## 定义使用版本

```shell
export ETCDCTL_API=3
```

## 存储键值对

```shell
etcdctl put key value 
```

从宿主机取

```shell
cat ./global_config.yaml | docker-compose exec -T enjoyfood-backend-etcd sh -c "export ETCDCTL_API=3 && etcdctl put /enjoyfood-backend/global_config"
```

## 删除键值对

```shell
etcdctl del key
```

## 获取所有键值对

* --prefix=""：指定前缀为空字符串，这将包括所有键。
* --keys-only=false：确保除了键之外，也返回键的值。
* "/"：指定根目录作为要检索的键的前缀。

```shell
etcdctl get --prefix="" --keys-only=false "/"

```

以 / 为前缀

```shell
etcdctl get --prefix /
```