# elastic

<!-- TOC -->

* [elastic](#elastic)
    * [启动](#启动)
        * [生成token](#生成token)
        * [verify](#verify)
        * [获取密码](#获取密码)
        * [关闭ssl](#关闭ssl)
    * [使用](#使用)
        * [当前节点、集群、版本](#当前节点集群版本)
        * [查看所有索引](#查看所有索引)
        * [创建索引](#创建索引)
        * [查看索引信息](#查看索引信息)
        * [](#)

<!-- TOC -->

## 启动

### 生成token

```shell
bin/elasticsearch-create-enrollment-token --scope kibana
```

### verify

```shell
bin/kibana-verification-code
```

### 获取密码

```shell
bin/elasticsearch-reset-password -u elastic
```

### 关闭ssl

```
 /usr/share/elasticsearch/config/elasticsearch.yml
```

## 使用

### 当前节点、集群、版本

```shell
curl localhost:9200
```

### 查看所有索引

```shell
curl -XGET "localhost:9200/_cat/indices"
```

### 创建索引

```shell
curl -XPUT "http://localhost:9200/my-index-000001" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "index": {
      "number_of_shards": 3,
      "number_of_replicas": 2
    }
  }
}'
```

### 查看索引信息

```shell
curl -XGET "http://localhost:9200/my-index-000001/_search?pretty=true" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match_all": {}
  }
}
'
```

