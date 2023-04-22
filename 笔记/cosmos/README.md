# cosmos
<!-- TOC -->
* [cosmos](#cosmos)
  * [启动项目](#启动项目)
  * [查看命令](#查看命令)
  * [查询所有用户](#查询所有用户)
  * [查询余额](#查询余额)
  * [转账](#转账)
  * [查询交易](#查询交易)
  * [添加账户](#添加账户)
  * [查看用户私钥](#查看用户私钥)
<!-- TOC -->

##  启动项目
```shell
tntchaind start
```
##  查看命令
```shell
tntchaind query bank balances -h
```
##  查询所有用户
```shell
tntchaind keys list

```
##  查询余额
```shell
tntchaind query bank balances cosmos12ljuv8t4w20cc784wajp98cexwwstjntkyc4a4
```

##  转账
```shell
tntchaind tx bank send cosmos12ljuv8t4w20cc784wajp98cexwwstjntkyc4a4  cosmos1wk8e33pncg76jm5484hrm8vacf6xt8xjr98k66 1000TNT   
```

##  查询交易
```shell
tntchaind  query txs --events transfer.sender=cosmos1zasd5z03g2yvnpvvnlxu3wk2zqzrzcy4e7cpjc
```

##  添加账户
```shell
tntchaind keys add  zwz
```
## 查看用户私钥
```shell
tntchaind     keys      export     zhangsan   --unarmored-hex   --unsafe 
```
