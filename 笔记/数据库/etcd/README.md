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
cat /Users/zhouwenzhe/src/yuhuProject/Qilin/deploy/qilin-zwz-docker-compose/global_config.yaml | docker exec -i zwz-env-etcd-1 sh -c "export ETCDCTL_API=3 && etcdctl put /qilin/global_config"
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
export ETCDCTL_API=3
etcdctl get --prefix /
```

## 查看版本
```shell
export endpoint=127.0.0.1:2379
export key=$(echo -n "/zwz/test" | base64)
export value=$(cat /Users/zhouwenzhe/src/yuhuProject/Qilin/deploy/qilin-zwz-docker-compose/global_config.yaml | base64)
```
```shell
curl http://$endpoint/version
```
## 查看key的值
```shell
curl  http://$endpoint/v3/kv/range -X POST -d "{\"key\": \"$key\"}"| jq -r '.kvs[0].value' | base64 -d
```
## 设置key的值
```shell
curl http://$endpoint/v3/kv/put -X POST -d "{\"key\": \"$key\", \"value\": \"$value\"}"
```