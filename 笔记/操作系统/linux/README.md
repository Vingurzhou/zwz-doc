# linux

<!-- TOC -->

- [linux](#linux)
  - [连接管理](#连接管理)
    - [连接](#连接)
      - [Kali Linux 6.1.0](#kali-linux-610)
      - [Ubuntu 22.04.2](#ubuntu-22042)
      - [Ubuntu 16.04.5 LTS](#ubuntu-16045-lts)
    - [生成 SSH 公钥和私钥](#生成-ssh-公钥和私钥)
    - [将公钥复制到云服务器上](#将公钥复制到云服务器上)
  - [系统管理](#系统管理)
    - [设置主机名](#设置主机名)
    - [重启](#重启)
    - [查看内网 ip](#查看内网-ip)
    - [查看版本](#查看版本)
    - [查看 cpu 核数](#查看-cpu-核数)
    - [查看架构](#查看架构)
  - [文件管理](#文件管理)
    - [查看文件占用率](#查看文件占用率)
    - [查看目录](#查看目录)
    - [创建文件](#创建文件)
    - [移动文件](#移动文件)
    - [删除文件](#删除文件)
    - [查找文件](#查找文件)
    - [下载远程文件](#下载远程文件)
    - [上传本地文件](#上传本地文件)
    - [复制文件夹](#复制文件夹)
    - [按关键字查找](#按关键字查找)
    - [查看文件最新输出](#查看文件最新输出)
    - [显示隐藏文件](#显示隐藏文件)
    - [批量替换字符](#批量替换字符)
    - [添加权限](#添加权限)
  - [进程管理](#进程管理)
    - [查看占用端口进程](#查看占用端口进程)
    - [查看进程占用端口](#查看进程占用端口)
    - [查看进程启动命令](#查看进程启动命令)
    - [查看命令启动进程](#查看命令启动进程)
    - [关闭进程](#关闭进程)
    - [根据端口删除](#根据端口删除)
  - [shell 管理](#shell-管理)
    - [查看 shell](#查看-shell)
    - [查看 bash shell 可执行文件](#查看-bash-shell-可执行文件)
    - [环境变量](#环境变量)
  - [vim](#vim)
    - [查找](#查找)
    - [批量替换](#批量替换)
    - [清空](#清空)
  - [防火墙管理](#防火墙管理)
    - [查看防火墙状态](#查看防火墙状态)
    - [允许防火墙端口](#允许防火墙端口)
  - [网络管理](#网络管理)
    - [查看网络](#查看网络)
  - [其他](#其他)
    - [解析 json](#解析-json)
    - [清除 DNS 缓存](#清除-dns-缓存)
    - [拷贝 Bearer token 到剪贴板](#拷贝-bearer-token-到剪贴板)
    - [查看历史命令](#查看历史命令)
  - [apt-get 500](#apt-get-500)
  - [提升删除速度](#提升删除速度)
  - [保持不断开](#保持不断开)
  - [检查磁盘空间](#检查磁盘空间)

## 连接管理

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

#### Ubuntu 16.04.5 LTS

```shell
ssh root@119.3.106.151
```

### 生成 SSH 公钥和私钥

```shell
ssh-keygen -t rsa
open ~/.ssh
```

### 将公钥复制到云服务器上

```shell
ssh-copy-id -p 33789 root@3.85.110.97
```

## 系统管理

### 设置主机名

```shell
hostnamectl set-hostname master
```

### 重启

```shell
sudo reboot
```

### 查看内网 ip

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

### 查看 cpu 核数

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

## 文件管理

### 查看文件占用率

```shell
df -h
```

### 查看目录

```shell
tree -L 2 /Users/zhouwenzhe/src/practiceProject/Untitled/EyouCMS-V1.5.1-UTF8-SP3
```

### 创建文件

```shell
mkdir -p ~/.enjoyfood-data/data/file/system/10/13/9 && touch ~/.enjoyfood-data/data/file/system/10/13/9/9Wj7XDmrjByx.glb


```

### 移动文件

```shell
mv /Users/zhouwenzhe/Downloads/WX20230817-134339@2x.png ～/.enjoyfood-data/data/file/system/9/15/5/GDoZROMovroq.png

```

### 删除文件

```shell
rm -rf
```

### 查找文件

```shell
find  ~ -name daemon.json
```

```shell
#find /Users/zhouwenzhe -regex "*.c"
find / -path "*/file/system/*" -type f
```

### 下载远程文件

```shell
scp -P 22 -r lighthouse@43.129.80.158:/home/lighthouse/v2.enjoyfood-backend/pkg/prisma /Users/zhouwenzhe/src/yuhuProject/v2.enjoyfood-backend/pkg
```

```shell
scp -P 22 -r root@119.3.106.151:/root/v2.enjoyfood-backend/deploy/enjoyfood-backend-v10.4.4-docker-compose-test/优化后1.log /Users/zhouwenzhe/src/yuhuProject/v2.enjoyfood-backend
```

### 上传本地文件

```shell
scp -P 22 -r /Users/zhouwenzhe/src/yuhuProject/v2.enjoyfood-backend/prisma/assets-prisma lighthouse@43.129.80.158:/home/lighthouse/v2.enjoyfood-backend/prisma
scp -P 22 -r /Users/zhouwenzhe/src/yuhuProject/v2.enjoyfood-backend/pkg/prisma lighthouse@43.129.80.158:/home/lighthouse/v2.enjoyfood-backend/pkg
```

### 复制文件夹

```shell
cp -r /home/laoxiao/tntchain /home/laoxiao/zwz/youyaProject/tntchain
```

### 按关键字查找

```shell
grep -r 1 .
docker ps | grep assets
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

命令“chmod o+w filename”用于更改类 Unix 操作系统中文件的权限，向“其他”(o) 用户授予写 (w)
权限。换句话说，它允许不是文件所有者或非文件关联组成员的用户写入该文件。

类 Unix 系统中的每个文件都具有三种类型的权限：读 (r)、写 (w) 和执行 (x)。这些权限被分配给三类用户：文件的所有者 (u)
、与文件关联的组 (g) 和其他人 (o)。

```shell
chmod o+x kubeadm kubelet kubectl
```

```shell
chmod zwz 401 /home
```

## 进程管理

### 查看占用端口进程

```shell
lsof -i:10257
```

### 查看进程占用端口

```shell
lsof -p 11086 -i -P -n | grep LISTEN
```

### 查看进程启动命令

```shell
ps -p 11086 -f
```

### 查看命令启动进程

```shell
ps aux | grep 'kubectl'
```

### 关闭进程

```shell
kill 73309
```

### 根据端口删除

```shell
kill $(lsof -t -i:2380)
```

## shell 管理

### 查看 shell

```shell
echo $SHELL
```

### 查看 bash shell 可执行文件

```shell
compgen -c

```

### 环境变量

```shell
echo 'export PATH="/opt/homebrew/Cellar/protobuf@3.6/3.6.1.3_4/bin:$PATH"' >> ~/.zshrc
#echo 'export PATH=/your/directory/path:$PATH' >> ~/.zshrc
source ~/.zshrc
printenv
```

```shell
echo 'export PATH="/opt/homebrew/Cellar/protobuf@3.6/3.6.1.3_4/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc
```

## vim

### 查找

1. 在正常模式下按 / 键
2. 输入要搜索的字符串 stake
3. 按下 Enter 键
   这将在当前文档中搜索字符串 stake，并将光标移动到第一个匹配项处。要查找下一个匹配项，请按 n 键。要查找上一个匹配项，请按 N
   键。

另外，如果你想要查找当前光标所在位置后面的第一个匹配项，可以使用 \*
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

## 网络管理

### 查看网络

```shell
netstat
```

## 其他

### 解析 json

```shell
echo '{"name": "John", "age": 30}' | jq '.'
```

### 清除 DNS 缓存

```shell
dscacheutil -flushcache
killall -HUP mDNSResponder
```

### 拷贝 Bearer token 到剪贴板

```shell
username=chenqing; pwd=admin123; echo 'Bearer' `curl -X POST "http://119.3.106.151:10200/v1/oauth2/token" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"grant_type\": \"password\", \"client_id\": \"PC\", \"client_secret\": \"\", \"scope\": \"\", \"username\": \"${username}\", \"password\": \"${pwd}\", \"refresh_token\": \"\", \"code\": \"\", \"reg_id\": \"\", \"platform_type\": 0}"|jq -r '.access_token'` | pbcopy
```

### 查看历史命令

```shell
history
```

```shell
history -c
```

## apt-get 500

关掉 vpn 代理

## 提升删除速度

```shell
defaults write NSGlobalDomain KeyRepeat -int 1
defaults write NSGlobalDomain InitialKeyRepeat -int 15
```

第一行的 KeyRepeat 对应的是「按键重复」，系统设置里调到最快对应的值是 2，你可以调成 0 或者 1（建议调为 1，0 可能会太快）；
第二行的 InitialKeyRepeat 对应的是「重复前延迟」，系统设置里调到最快对应的值是 15，你可以尝试调成 10 或者更小，不过我还是建议保持 15，因为反应时间太快会容易导致误操作（比如 Esc 键和 Command-Z 这样的快捷键）；

## 保持不断开

```shell
while true; do echo 1; sleep 10; done
```

## 检查磁盘空间

```shell
df -h
```
