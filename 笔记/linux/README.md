# linux

<!-- TOC -->
* [linux](#linux)
  * [重启](#重启)
  * [删除文件夹](#删除文件夹)
  * [查找文件](#查找文件)
  * [下载文件夹](#下载文件夹)
  * [上传文件夹](#上传文件夹)
  * [连接](#连接)
  * [生成SSH公钥和私钥](#生成ssh公钥和私钥)
  * [将公钥复制到云服务器上](#将公钥复制到云服务器上)
  * [复制文件夹](#复制文件夹)
  * [查找关键字](#查找关键字)
  * [查看占用端口进程](#查看占用端口进程)
  * [查看进程占用端口](#查看进程占用端口)
  * [查看进程启动命令](#查看进程启动命令)
  * [关闭进程](#关闭进程)
  * [根据端口删除](#根据端口删除)
  * [查看shell](#查看shell)
  * [查看bash shell 可执行文件](#查看bash-shell-可执行文件)
  * [查看文件最新输出](#查看文件最新输出)
  * [查看系统版本信息](#查看系统版本信息)
  * [查看系统架构](#查看系统架构)
  * [显示隐藏文件](#显示隐藏文件)
  * [批量替换字符](#批量替换字符)
  * [vim](#vim)
    * [查找](#查找)
    * [批量替换](#批量替换)
<!-- TOC -->

## 重启

```shell
sudo reboot

```

## 删除文件夹

```shell
rm -rf

```

## 查找文件

```shell
find /Users/zhouwenzhe/go -name secp256k1

```

## 下载文件夹

```shell
scp -r laoxiao@192.168.1.156:/home/laoxiao/evmos /Users/zhouwenzhe/src/youyaProject
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

## 查看占用端口进程

```shell
lsof -i:26656
```

## 查看进程占用端口

```shell
lsof -p 1252447 -i -P -n | grep LISTEN
```

## 查看进程启动命令

```shell
ps -p 1252447 -f
```

```shell

```

## 关闭进程

```shell
kill 42365
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

## 查看文件最新输出

```shell
tail -f /opt/go/gopath/bin/tnt.log
```

## 查看系统版本信息

linux

```shell
cat /etc/os-release
```

mac

```shell  
sw_vers
```

## 查看系统架构

```shell
uname -m

```

## 显示隐藏文件

```shell
ls -a
```

## 批量替换字符

```shell
sed -i 's/stake/TNT/g' file.txt
```

## vim

### 查找

1. 在正常模式下按 / 键
2. 输入要搜索的字符串 stake
3. 按下 Enter 键
   这将在当前文档中搜索字符串 stake，并将光标移动到第一个匹配项处。要查找下一个匹配项，请按 n 键。要查找上一个匹配项，请按 N
   键。

另外，如果你想要查找当前光标所在位置后面的第一个匹配项，可以使用 *
键。如果你想要查找当前光标所在位置前面的第一个匹配项，可以使用 # 键。

### 批量替换

`:%s/stake/TNT/g`

1. 在正常模式下按 : 键，进入命令行模式。
2. 输入 %s/stake/TNT/g 命令，其中 % 表示对整个文档进行替换，s 表示进行替换操作，/stake/ 表示要被替换的字符串，TNT
   表示替换后的字符串，g 表示进行全局替换，即每个匹配的字符串都会被替换。
3. 按下 Enter 键，执行替换操作。
   注意，在执行替换操作之前，建议先备份原始文件，以避免误操作导致数据丢失。如果需要确认每个替换操作，可以将命令中的 g 参数去掉，这样
   Vim 会在每个匹配处停下来等待确认。