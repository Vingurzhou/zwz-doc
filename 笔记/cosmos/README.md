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
  * [初始化区块链](#初始化区块链)
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
tntchaind tx bank send cosmos12ljuv8t4w20cc784wajp98cexwwstjntkyc4a4  cosmos14v9estvzfxjw8y38sd559dnxh2a33ww9hdaduz 1000000TNT   
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
tntchaind     keys      export     alice   --unarmored-hex   --unsafe 
```

## 初始化区块链
```shell
tntchaind init tntchain
tntchaind keys add zwz
tntchaind add-genesis-account zwz 100000000stake --keyring-backend os
tntchaind gentx zwz 70000000stake --chain-id tntchain
tntchaind start

```