# cosmos

<!-- TOC -->

* [cosmos](#cosmos)
    * [术语](#术语)
    * [创建单个验证器节点](#创建单个验证器节点)
    * [启动项目](#启动项目)
    * [查看命令](#查看命令)
    * [查询所有用户](#查询所有用户)
    * [生成新的密钥/助记符](#生成新的密钥助记符)
    * [evmos 密钥导出为以太坊私钥](#evmos-密钥导出为以太坊私钥)
    * [查看节点配置](#查看节点配置)
    * [查看帐户余额](#查看帐户余额)
    * [创建、签名、广播 交易](#创建签名广播-交易)
    * [查询交易](#查询交易)

<!-- TOC -->

## 术语

| 缩写         | 全称          | 含义                                                                                                                                                                                                                                                                       |
|------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| secret key | secret key  | 秘钥、对称密钥                                                                                                                                                                                                                                                                  |
| priv_key   | Private Key | 私钥、非对称密钥                                                                                                                                                                                                                                                                 |
| Moniker    | Moniker     | 别名，描述一个人或物体的称呼或标签，通常是由某些特征或行为引起的                                                                                                                                                                                                                                         |
| validator  | validator   | 验证节点，也称为验证者或验证人                                                                                                                                                                                                                                                          |
| genesis    | genesis     | 创世                                                                                                                                                                                                                                                                       |
| Pruning    | Pruning     | 剪枝，通常指的是从区块链的历史记录中删除旧的或者无用的数据，以减少整个区块链网络的存储空间和资源消耗。由于区块链是一个分布式的数据库，每个节点都需要存储所有的交易记录和区块信息。但是，随着时间的推移，区块链的数据量将不断增长，这可能导致存储和传输数据的成本和复杂度不断增加。为了解决这个问题，一些区块链采用了剪枝技术，通过删除旧的或者无用的数据来减少整个区块链的存储空间和资源消耗。剪枝技术通常是在保证区块链安全性和可靠性的前提下实现的，例如通过保留区块链的核心数据和验证信息，同时删除不必要的交易记录和区块信息来减少存储空间。 |
| delegation | delegation  | 委托，通常指的是将代币或者权益授权给其他节点或者用户，让他们代表自己进行验证、投票、治理等活动                                                                                                                                                                                                                          |
| stake      | stake       | 权益，通常指代那些被用于参与区块链共识机制的代币或者数字资产                                                                                                                                                                                                                                           |
| gas        | gas         | 燃料,通常是指一种用于支付区块链交易手续费的计量单位。每个区块链交易都需要一定的计算和存储资源来执行和保存，这些资源消耗将由发起交易的用户支付                                                                                                                                                                                                  |
| evidence   | evidence    | 证据,通常指的是用于证明某个事实或事件发生的数据或信息                                                                                                                                                                                                                                              |
| Denom      | Denom       | 面值,通常指代数字资产或代币的面值或单位                                                                                                                                                                                                                                                     |
| Fee        | Fee         | 费用，通常指代支付给验证者或矿工的交易手续费                                                                                                                                                                                                                                                   |
| granter    | granter     | 授权者,是指在某些区块链网络中，拥有授权权限的账户或实体，可以授权其他账户或实体在其名下进行某些操作或行为                                                                                                                                                                                                                    |
| signatures | signatures  | 签名,通常指交易的数字签名，它是一种数字化的加密方式，用于验证交易的合法性和完整性                                                                                                                                                                                                                                |
|            |             |                                                                                                                                                                                                                                                                          |
|            |             |                                                                                                                                                                                                                                                                          |

## 创建单个验证器节点

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

## 启动项目

```shell
tntchaind start
```

## 查看命令

```shell
evmosd  -h
```

## 查询所有用户

```shell
evmosd keys list \
--home ~/.tmp-evmosd \
--keyring-backend test
```

## 生成新的密钥/助记符

```shell
evmosd keys add zwz \
--home ~/.tmp-evmosd \
--keyring-backend test
```

## evmos 密钥导出为以太坊私钥

```shell
evmosd keys unsafe-export-eth-key zwz \
--home ~/.tmp-evmosd \
--keyring-backend test
```

## 查看节点配置

```shell
evmosd config \
--home ~/.tmp-evmosd
```

## 查看帐户余额

```shell
evmosd q bank balances \
evmos1x6cx9236nrsgkyea483nxjtquwdp8u6ru06c8p \
--home ~/.tmp-evmosd
```

## 创建、签名、广播 交易

```shell
evmosd tx bank send \
  evmos1x6cx9236nrsgkyea483nxjtquwdp8u6ru06c8p \
  evmos1a7zne7vu9u35awns9vypjy8endmu7zf2j74crk \
  1aevmos \
  --home ~/.tmp-evmosd \
  --fees 50000000000aevmos \
  --broadcast-mode block

```

## 查询交易

```shell
evmosd  query txs \
--events transfer.sender=evmos1x6cx9236nrsgkyea483nxjtquwdp8u6ru06c8p
```
