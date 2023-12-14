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
  * [拷贝文件](#拷贝文件)
  * [执行命令](#执行命令)
  * [dockerfile](#dockerfile)
    * [保持运行不退出](#保持运行不退出)
  * [根据tar构建镜像](#根据tar构建镜像)
  * [释放网络](#释放网络)
  * [显示映像中的漏洞](#显示映像中的漏洞)
  * [交叉编译](#交叉编译)
<!-- TOC -->

## 找错

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

## 查看网络

网络的IP地址范围是"172.27.0.0/16"。这意味着在该网络中，可以使用从172.27.0.0到172.27.255.255之间的IP地址。

IP地址范围"172.27.0.0/16"是一个私有IP地址范围，通常在Docker默认网络或自定义网络中使用。你可以在该网络中为容器分配IP地址，并允许它们进行通信。

需要注意的是，网络的子网掩码为16，这表示网络中有65536个可用的IP地址。

```shell
docker network ls
docker network inspect vue_default

```
## 查新容器信息
```shell
docker inspect 6ecbc68620b1
```
## 运行容器

```shell
docker run -p 80:80 -d $(docker build -q .)
```

```shell
docker run -d \
--name zwz-admin-api \
--privileged \
--restart always \
-p 8000:8000 \
-v ./config/:/go-admin-api/config/ \
-v ./static/:/go-admin-api/static/ \
-v ./temp/:/go-admin-api/temp/ \
-e TZ=Asia/Shanghai \
--network backend \
vingurzhou/zwz-admin:latest

```

## 启动容器

```shell
docker start
```
```shell
/usr/local/bin/docker-compose -f /Users/zhouwenzhe/src/zwz-env/docker-compose.yml up -d redis
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

## 拷贝文件

```shell
docker cp /Users/zhouwenzhe/src/yuhuProject/v2.enjoyfood-backend/sources.list enjoyfood-backend-system-manager:/etc/apt
```

## 执行命令
ls


```shell
docker exec -it zwz-env-golang13-1 sh -c "cd /Users/zhouwenzhe/src/yuhuProject/v2.enjoyfood-backend && go build -o ./build ./cmd/..."

```

## dockerfile

### 保持运行不退出

```
tail -f /dev/null
```

##  根据tar构建镜像
```shell
docker load -i centos.tar
docker commit -a "易波涵" -m "gcc-arm" 容器id armgcc:1.0
docker save -o gcc-arm.tar 镜像id
```

## 释放网络
```shell
docker network disconnect -f enjoyfood-backend-v1042-docker-compose-test_default enjoyfood-backend-iam-cron
```
## 显示映像中的漏洞
它显示映像中的漏洞以及基础映像中的漏洞的摘要。如果可用，它还会显示基础映像刷新和更新建议。

```shell
docker scout quickview dnorange/prisma-cli:1.34.7 
```

## 交叉编译
```shell
docker buildx create --name mybuilder
docker buildx use mybuilder
docker buildx build --platform linux/amd64 -t chaoyue/kubecit-service --push .

```

## 设置配置

```shell
open -a Goland /Users/zhouwenzhe/.docker/daemon.json
```

## 清理未使用的资源
```shell
docker system prune -a
# 删除所有停止的容器
#docker container prune
# 删除所有未使用的镜像
#docker image prune -a
```