# grpc
<!-- TOC -->
* [grpc](#grpc)
  * [安装 grpcurl](#安装-grpcurl)
  * [查看gRPC 服务列表](#查看grpc-服务列表)
  * [获得服务的描述](#获得服务的描述)
  * [查询节点信息](#查询节点信息)
<!-- TOC -->
## 安装 grpcurl

```shell
go install github.com/fullstorydev/grpcurl/cmd/grpcurl@latest
```

## 查看gRPC 服务列表

```shell
grpcurl -plaintext localhost:9090 list
```

## 获得服务的描述

```shell
grpcurl -plaintext \
    localhost:9090 \
    describe tntchain.tntchain.Query
```

## 查询节点信息

```shell
grpcurl \
    -plaintext \
    -d "{\"address\":\"cosmos1a62h0l97s9jr4v57nfl2hv2u9tu90k7789sfnx\"}" \
    localhost:9090 \
    cosmos.bank.v1beta1.Query/AllBalances
```