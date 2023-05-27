# docker

<!-- TOC -->
* [docker](#docker)
  * [重新构建](#重新构建)
  * [禁用缓存机制](#禁用缓存机制)
  * [保持运行不退出](#保持运行不退出)
<!-- TOC -->

## 重新构建

```shell
/usr/local/bin/docker-compose -f \
/Users/zhouwenzhe/src/tendermint-explorer/docker-compose.yml \
up --build
```

## 禁用缓存机制

```shell
/usr/local/bin/docker-compose -f \
/Users/zhouwenzhe/src/zwz-admin/docker-compose.yml \
build --no-cache
```

##  保持运行不退出
```dockerfile
tail -f /dev/null
```