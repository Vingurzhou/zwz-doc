# linux

<!-- TOC -->
* [linux](#linux)
  * [删除文件夹](#删除文件夹)
  * [查找文件](#查找文件)
  * [下载文件夹](#下载文件夹)
  * [上传文件夹](#上传文件夹)
  * [连接](#连接)
  * [生成SSH公钥和私钥](#生成ssh公钥和私钥)
  * [将公钥复制到云服务器上](#将公钥复制到云服务器上)
  * [复制文件夹](#复制文件夹)
  * [查找关键字](#查找关键字)
  * [查看端口占用](#查看端口占用)
  * [关闭进程](#关闭进程)
  * [根据端口删除](#根据端口删除)
  * [查看shell](#查看shell)
  * [查看bash shell 可执行文件](#查看bash-shell-可执行文件)
  * [查看文件最新输出](#查看文件最新输出)
<!-- TOC -->

## 删除文件夹

```shell
rm -rf

```

## 查找文件

```shell
find . -name app.go

```

## 下载文件夹

```shell
scp -r laoxiao@192.168.1.156:/home/laoxiao/zwz/youyaProject /Users/zhouwenzhe/src
```

## 上传文件夹

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

## 复制文件夹

```shell
cp -r /home/laoxiao/tntchain /home/laoxiao/zwz/youyaProject/tntchain
```

## 查找关键字

```shell
grep -r keyword .
```

## 查看端口占用

```shell
lsof -i:1317
```

## 关闭进程

```shell
kill 86341
```

## 根据端口删除

```shell
kill $(lsof -t -i:1001)
```

## 查看shell

```shell
echo $SHELL
```

## 查看bash shell 可执行文件
```shell
compgen -c

```
##  查看文件最新输出
```shell
tail -f /opt/go/gopath/bin/tnt.log
```