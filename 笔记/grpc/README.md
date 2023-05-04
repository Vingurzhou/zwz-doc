# grpc
<!-- TOC -->
* [grpc](#grpc)
  * [安装工具](#安装工具)
  * [Protocol Buffer](#protocol-buffer)
    * [下载文件](#下载文件)
    * [编写文件](#编写文件)
  * [protoc](#protoc)
    * [使用命令](#使用命令)
  * [grpcurl](#grpcurl)
    * [查看gRPC 服务列表](#查看grpc-服务列表)
    * [获得服务的描述](#获得服务的描述)
    * [查询节点信息](#查询节点信息)
<!-- TOC -->
## 安装工具
```shell
#grpcurl
go install github.com/fullstorydev/grpcurl/cmd/grpcurl@latest
#protoc
go install google.golang.org/protobuf/cmd/protoc-gen-go
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc
#grpc-gateway
go install github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-grpc-gateway
go install github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-openapiv2

```

##  Protocol Buffer
### [下载文件](https://github.com/googleapis/googleapis)
地址： https://github.com/googleapis/googleapis
### 编写文件
```protobuf
syntax = "proto3";
package helloworld;
//import "google/api/annotations.proto";
option go_package = "proto/helloworld";
service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply) {
//    option (google.api.http) = {
//      post: "/v1/example/echo"
//      body: "*"
    };
  }
}
message HelloRequest {
  string name = 1;
}
message HelloReply {
  string message = 1;
}
```
##  protoc
### 使用命令
```shell
protoc --proto_path=./proto \
  --proto_path=/Users/zhouwenzhe/go/pkg/mod/github.com/googleapis/gnostic@v0.5.5/third_party  \
  --go_out=../  \
  --go_opt=paths=import \
  --go-grpc_out=../ \
  --go-grpc_opt=paths=import  \
  --grpc-gateway_out=../  \
  --grpc-gateway_opt=paths=import \
  --openapiv2_out=./docs/static  \
  --openapiv2_opt=allow_merge=true  \
  --openapiv2_opt=merge_file_name=openapi  \
  ./proto/tntchain/tntchain/extend.proto

```
##  grpcurl
### 查看gRPC 服务列表

```shell
grpcurl -plaintext localhost:9090 list
```

### 获得服务的描述

```shell
grpcurl -plaintext \
    localhost:9090 \
    describe tntchain.tntchain.Query
```

### 查询节点信息

```shell
grpcurl \
    -plaintext \
    -d "{\"address\":\"cosmos1a62h0l97s9jr4v57nfl2hv2u9tu90k7789sfnx\"}" \
    localhost:9090 \
    cosmos.bank.v1beta1.Query/AllBalances
```
