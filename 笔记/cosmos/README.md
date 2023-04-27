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
tntchaind query bank balances cosmos1j43332jly9vkk86ne6umsdqkrtphmcx0tpyd03
```

##  转账
```shell
tntchaind tx bank send cosmos1834vgx58uzl4dqa97ht78ulrnrgwkhx4zfwcmm  cosmos1j43332jly9vkk86ne6umsdqkrtphmcx0tpyd03 1000TNT   
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
rm -rf ~/.tntchain/
tntchaind init tntchain  --staking-bond-denom TNT
tntchaind keys add zwz --keyring-backend os
tntchaind add-genesis-account zwz 100000000TNT --keyring-backend os
tntchaind gentx zwz 70000000TNT --keyring-backend os
tntchaind collect-gentxs
vim ~/.tntchain/config/app.toml
tntchaind start

```