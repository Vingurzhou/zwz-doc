# cosmos

<!-- TOC -->
* [cosmos](#cosmos)
  * [术语](#术语)
  * [创建单个验证器节点](#创建单个验证器节点)
  * [查看命令](#查看命令)
  * [查询所有用户](#查询所有用户)
  * [生成新的密钥/助记符](#生成新的密钥助记符)
  * [evmos 密钥导出为以太坊私钥](#evmos-密钥导出为以太坊私钥)
  * [查看节点配置](#查看节点配置)
  * [查看帐户余额](#查看帐户余额)
  * [创建、签名、广播 交易](#创建签名广播-交易)
  * [查询交易](#查询交易)
  * [转换地址为十六进制和bech32格式](#转换地址为十六进制和bech32格式)
  * [获取地址公钥](#获取地址公钥)
  * [查询账户信息](#查询账户信息)
  * [恢复公钥](#恢复公钥)
<!-- TOC -->

## 术语

| 缩写         | 全称                             | 含义                                                     |
|------------|--------------------------------|--------------------------------------------------------|
| secret key | secret key                     | 秘钥、对称密钥                                                |
| priv_key   | Private Key                    | 私钥、非对称密钥                                               |
| Moniker    | Moniker                        | 别名，描述一个人或物体的称呼或标签，通常是由某些特征或行为引起的                       |
| validator  | validator                      | 验证节点，也称为验证者或验证人                                        |
| genesis    | genesis                        | 创世                                                     |
| Pruning    | Pruning                        | 剪枝，通常指的是从区块链的历史记录中删除旧的或者无用的数据，以减少整个区块链网络的存储空间和资源消耗     |
| delegation | delegation                     | 委托，通常指的是将代币或者权益授权给其他节点或者用户，让他们代表自己进行验证、投票、治理等活动        |
| stake      | stake                          | 权益，通常指代那些被用于参与区块链共识机制的代币或者数字资产                         |
| gas        | gas                            | 燃料,通常是指一种用于支付区块链交易手续费的计量单位                             |
| evidence   | evidence                       | 证据,通常指的是用于证明某个事实或事件发生的数据或信息                            |
| Denom      | Denom                          | 面值,通常指代数字资产或代币的面值或单位                                   |
| Fee        | Fee                            | 费用，通常指代支付给验证者或矿工的交易手续费                                 |
| granter    | granter                        | 授权者,是指在某些区块链网络中，拥有授权权限的账户或实体，可以授权其他账户或实体在其名下进行某些操作或行为  |
| signatures | signatures                     | 签名,通常指交易的数字签名，它是一种数字化的加密方式，用于验证交易的合法性和完整性              |
| Ledger     | Distributed Ledger             | 分布式账本，它是一种基于区块链技术的分散式数据库，用于记录和存储所有交易信息                 |
| HD         | Hierarchical Deterministic Key | 分层确定性密钥，它是一种基于数学算法的加密机制，用于生成一组有序的公私钥对，同时可以方便地创建多个子钱包   |
| Sequence   | Sequence                       | 交易的序列号                                                 |
| chainid    | Chain Identifier               | 链标识符或链身份标识                                             |
| Protobuf   | Protocol Buffers               | 协议缓冲区，语言无关、平台无关、可扩展的序列化数据结构和协议的方法，用于数据交换、存储和通信         |
| RLP        | Recursive Length Prefix        | 递归长度前缀，RLP是一种用于编码任意复杂度的数据结构的序列化方法，旨在提供高效、紧凑和可扩展的数据表示方式 |
| Mnemonic   | Mnemonic                       | 助记词                                                    |
| denom      | denomination                   | 即代币或数字资产的单位或面值                                         |
|            |                                |                                                        |

## 创建单个验证器节点

```shell
rm -rf ~/.tntchain/
tntchaind init tntchain  --staking-bond-denom TNT
tntchaind keys add zwz --keyring-backend os
tntchaind add-genesis-account zwz 10000000000000000000000000000000TNT --keyring-backend os
tntchaind gentx zwz 70000000TNT --keyring-backend os
tntchaind collect-gentxs
vim ~/.tntchain/config/app.toml
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

## 查看账户余额

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
  --broadcast-mode block \
  --gas=auto

```

## 查询交易

```shell
evmosd  query txs \
--events transfer.sender=evmos1x6cx9236nrsgkyea483nxjtquwdp8u6ru06c8p
```

## 转换地址为十六进制和bech32格式

```shell
evmosd debug addr evmos1a7zne7vu9u35awns9vypjy8endmu7zf2j74crk
evmosd  debug addr EF853CF99C2F234EBA702B081910F99B77CF092A
```

## 获取地址公钥

```shell
evmosd keys show dev0 --bech acc   --home ~/.tmp-evmosd --keyring-backend test
evmosd keys show dev0 --bech val  --home ~/.tmp-evmosd --keyring-backend test
evmosd keys show dev0 --bech cons --home ~/.tmp-evmosd --keyring-backend test
```

## 查询账户信息

```shell
evmosd q auth account $(evmosd keys show dev0 -a  --home ~/.tmp-evmosd --keyring-backend test) -o text  --home ~/.tmp-evmosd --keyring-backend test
```

## 恢复公钥

```shell
evmosd keys add zwz-restored --recover --home ~/.tmp-evmosd --keyring-backend test
```