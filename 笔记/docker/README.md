# docker

<!-- TOC -->
* [docker](#docker)
  * [重新构建](#重新构建)
  * [禁用缓存机制](#禁用缓存机制)
<!-- TOC -->

## 重新构建

```shell
/usr/local/bin/docker-compose -f \
/Users/zhouwenzhe/Documents/go-admin-ui-master/docker-compose.yml \
up --build
```

## 禁用缓存机制

```shell
/usr/local/bin/docker-compose -f \
/Users/zhouwenzhe/Documents/go-admin-ui-master/docker-compose.yml \
build --no-cache
```