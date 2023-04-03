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
scp -r ./zwz laoxiao@192.168.1.156:/home/laoxiao/zwz
```