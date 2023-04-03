# linux

<!-- TOC -->
* [linux](#linux)
  * [删除文件夹](#删除文件夹)
  * [查找文件](#查找文件)
  * [下载](#下载)
  * [上传](#上传)
<!-- TOC -->

## 删除文件夹

```shell
rm -rf

```

## 查找文件

```shell
find . -name app.go

```

## 下载

```shell
scp -r laoxiao@192.168.1.156:/home/laoxiao/zwz .
```

## 上传

```shell
scp -r /Users/zhouwenzhe/src/youyaProject laoxiao@192.168.1.156:/home/laoxiao/zwz
```

## 连接
```shell
ssh laoxiao@192.168.1.156

```

## 生成SSH公钥和私钥
```shell
ssh-keygen -t rsa

```

## 将公钥复制到云服务器上
```shell
ssh-copy-id laoxiao@192.168.1.156
```