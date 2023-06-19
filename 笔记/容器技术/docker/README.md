# docker

<!-- TOC -->
* [docker](#docker)
  * [找错](#找错)
  * [登陆](#登陆)
  * [查看镜像](#查看镜像)
  * [构建镜像](#构建镜像)
  * [打包镜像](#打包镜像)
  * [推送镜像](#推送镜像)
  * [拉取镜像](#拉取镜像)
  * [删除镜像](#删除镜像)
  * [查看容器](#查看容器)
  * [创建网络](#创建网络)
  * [查看网络](#查看网络)
  * [运行容器](#运行容器)
  * [启动容器](#启动容器)
  * [进入容器bash](#进入容器bash)
  * [停止容器](#停止容器)
  * [删除容器](#删除容器)
  * [查看日志](#查看日志)
  * [dockerfile](#dockerfile)
    * [保持运行不退出](#保持运行不退出)
<!-- TOC -->

##  找错
```shell
dockerd --debug

```
## 登陆

```shell
docker login 
```

## 查看镜像

```shell
docker images 
docker images | grep zwz-admin

```

## 构建镜像

```shell
docker build --no-cache -t zwz-admin:latest --platform linux/amd64  /Users/zhouwenzhe/src/zwz-admin/
```

## 打包镜像

```shell
docker tag zwz-admin:latest vingurzhou/zwzadmin:latest
```

## 推送镜像

```shell
docker push vingurzhou/zwzadmin:latest
```

## 拉取镜像

```shell
docker pull vingurzhou/zwzadmin:latest

```

## 删除镜像

```shell
docker rmi c48ee48efd67
```

## 查看容器

```shell
docker ps -a
```

## 创建网络

```shell
docker network create backend

```
##  查看网络
网络的IP地址范围是"172.27.0.0/16"。这意味着在该网络中，可以使用从172.27.0.0到172.27.255.255之间的IP地址。

IP地址范围"172.27.0.0/16"是一个私有IP地址范围，通常在Docker默认网络或自定义网络中使用。你可以在该网络中为容器分配IP地址，并允许它们进行通信。

需要注意的是，网络的子网掩码为16，这表示网络中有65536个可用的IP地址。
```shell
docker network ls
docker network inspect vue_default

```
## 运行容器

```shell
docker run -d \
--name zwz-admin-api \
--privileged \
--restart always \
-p 8000:8000 \
-v ./config/:/go-admin-api/config/ \
-v ./static/:/go-admin-api/static/ \
-v ./temp/:/go-admin-api/temp/ \
--network backend \
vingurzhou/zwz-admin:latest

```

## 启动容器

```shell
docker start
```

## 进入容器bash

```shell
docker exec -it zwz-admin-ui  /bin/sh
```

## 停止容器

```shell
docker stop 4c76541794af
```

## 删除容器

```shell
docker rm zwz-admin
```

## 查看日志

```shell
docker logs zwz-admin
```

## dockerfile

### 保持运行不退出

```
tail -f /dev/null
```