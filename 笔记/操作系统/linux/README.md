# linux

<!-- TOC -->
* [linux](#linux)
  * [系统管理](#系统管理)
    * [设置主机名](#设置主机名)
    * [重启](#重启)
    * [查看内网ip](#查看内网ip)
    * [查看版本](#查看版本)
    * [查看cpu核数](#查看cpu核数)
    * [查看架构](#查看架构)
  * [连接管理](#连接管理)
    * [生成SSH公钥和私钥](#生成ssh公钥和私钥)
    * [将公钥复制到云服务器上](#将公钥复制到云服务器上)
    * [连接](#连接)
      * [Kali Linux 6.1.0](#kali-linux-610)
      * [Ubuntu 22.04.2](#ubuntu-22042)
  * [文件管理](#文件管理)
    * [查看目录](#查看目录)
    * [删除文件](#删除文件)
    * [查找文件](#查找文件)
    * [下载远程文件](#下载远程文件)
    * [上传本地文件](#上传本地文件)
    * [复制文件夹](#复制文件夹)
    * [按关键字查找](#按关键字查找)
    * [查看文件最新输出](#查看文件最新输出)
    * [显示隐藏文件](#显示隐藏文件)
    * [批量替换字符](#批量替换字符)
    * [添加权限](#添加权限)
  * [进程管理](#进程管理)
    * [查看占用端口进程](#查看占用端口进程)
    * [查看进程占用端口](#查看进程占用端口)
    * [查看进程启动命令](#查看进程启动命令)
    * [关闭进程](#关闭进程)
    * [根据端口删除](#根据端口删除)
  * [shell 管理](#shell-管理)
    * [查看shell](#查看shell)
    * [查看bash shell 可执行文件](#查看bash-shell-可执行文件)
    * [环境变量](#环境变量)
  * [vim](#vim)
    * [查找](#查找)
    * [批量替换](#批量替换)
    * [清空](#清空)
  * [防火墙管理](#防火墙管理)
    * [查看防火墙状态](#查看防火墙状态)
    * [允许防火墙端口](#允许防火墙端口)
  * [其他](#其他)
    * [解析json](#解析json)
    * [清除 DNS 缓存](#清除-dns-缓存)
<!-- TOC -->

## 系统管理

### 设置主机名

```shell
hostnamectl set-hostname master
```

### 重启

```shell
sudo reboot
```

### 查看内网ip

```shell
ifconfig
```

### 查看版本

```shell
cat /etc/os-release
cat /etc/redhat-release
cat /etc/release
cat /etc/version
```

### 查看cpu核数

```shell
# mac
#sysctl -n machdep.cpu.core_count

lscpu
#cat /proc/cpuinfo | grep "core id" | sort | uniq | wc -l
```

### 查看架构

```shell
uname -m
```

## 连接管理

### 生成SSH公钥和私钥

```shell
ssh-keygen -t rsa
```

### 将公钥复制到云服务器上

```shell
ssh-copy-id -p 33789 root@3.85.110.97 
```

### 连接

#### Kali Linux 6.1.0

```shell
ssh root@3.85.110.97 -p 33789
```

#### Ubuntu 22.04.2

```shell
ssh root@47.96.90.79 -p 22
```

```shell
ssh root@47.96.90.79 -p 22
```

```shell
ssh laoxiao@192.168.1.156 -p 22
```

```shell
ssh root@108.160.138.133 -p 22
```

```shell
ssh root@192.168.1.85 -p 22
```

```shell
ssh root@192.168.1.171 -p 22
```

## 文件管理

### 查看目录

```shell
tree -L 2 /Users/zhouwenzhe/src/practiceProject/Untitled/EyouCMS-V1.5.1-UTF8-SP3
```

### 删除文件

```shell
rm -rf 
```

### 查找文件

```shell
#find /Users/zhouwenzhe -regex "*.c"
sudo find /usr -path '*/python3' -type f 
```

### 下载远程文件

```shell
scp -r laoxiao@192.168.1.156:/home/laoxiao/evmos /Users/zhouwenzhe/src/youyaProject
```

### 上传本地文件

```shell
scp -P 33789 -r /Users/zhouwenzhe/src/practiceProject/Untitled root@3.85.110.97:/root
```

### 复制文件夹

```shell
cp -r /home/laoxiao/tntchain /home/laoxiao/zwz/youyaProject/tntchain
```

### 按关键字查找

```shell
grep -r 1 .
```

### 查看文件最新输出

```shell
tail -f /opt/go/gopath/bin/tnt.log
```

### 显示隐藏文件

```shell
ls -a
```

### 批量替换字符

```shell
sed -i 's/stake/TNT/g' file.txt
```

### 添加权限

```shell
chmod +x kubeadm kubelet kubectl
```

## 进程管理

### 查看占用端口进程

```shell
lsof -i:26657
```

### 查看进程占用端口

```shell
lsof -p 1252447 -i -P -n | grep LISTEN
```

### 查看进程启动命令

```shell
ps -p 7675 -f
```

### 关闭进程

```shell
kill 73309
```

### 根据端口删除

```shell
kill $(lsof -t -i:1001)
```

## shell 管理

### 查看shell

```shell
echo $SHELL
```

### 查看bash shell 可执行文件

```shell
compgen -c

```

### 环境变量

```shell
echo 'export PATH="/opt/homebrew/opt/node@16/bin:$PATH"' >> ~/.zshrc
#echo 'export PATH=/your/directory/path:$PATH' >> ~/.zshrc
source ~/.zshrc
printenv
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

### 清空

`:%d`

## 防火墙管理

### 查看防火墙状态

```shell
ufw status
```

### 允许防火墙端口

```shell
ufw allow 8081
```

## 其他

### 解析json

```shell
echo '{"name": "John", "age": 30}' | jq '.'
```

### 清除 DNS 缓存

```shell
dscacheutil -flushcache
killall -HUP mDNSResponder
```

