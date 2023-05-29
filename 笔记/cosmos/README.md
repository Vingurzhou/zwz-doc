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
  * [查看账户余额](#查看账户余额)
  * [创建、签名、广播 交易](#创建签名广播-交易)
  * [根据events查询交易](#根据events查询交易)
  * [根据hash查询交易](#根据hash查询交易)
  * [转换地址为十六进制和bech32格式](#转换地址为十六进制和bech32格式)
  * [获取地址公钥](#获取地址公钥)
  * [查询账户信息](#查询账户信息)
  * [恢复公钥](#恢复公钥)
  * [存储为变量](#存储为变量)
  * [模拟执行](#模拟执行)
  * [对base64解码](#对base64解码)
<!-- TOC -->

## 术语

| 缩写         | 全称                                             | 含义                                             |
|------------|------------------------------------------------|------------------------------------------------|
| secret key | secret key                                     | 秘钥、对称密钥                                        |
| priv_key   | Private Key                                    | 私钥、非对称密钥                                       |
| Moniker    | Moniker                                        | 别名，描述一个人或物体的称呼或标签                              |
| validator  | validator                                      | 验证节点，也称为验证者或验证人                                |
| genesis    | genesis                                        | 创世                                             |
| Pruning    | Pruning                                        | 剪枝，通常指的是从区块链的历史记录中删除旧的或者无用的数据                  |
| delegation | delegation                                     | 委托                                             |
| stake      | stake                                          | 权益，通常指代那些被用于参与区块链共识机制的代币或者数字资产                 |
| gas        | gas                                            | 燃料,通常是指一种用于支付区块链交易手续费的计量单位                     |
| evidence   | evidence                                       | 证据,通常指的是用于证明某个事实或事件发生的数据或信息                    |
| Fee        | Fee                                            | 费用，通常指代支付给验证者或矿工的交易手续费                         |
| granter    | granter                                        | 授权者                                            |
| signatures | signatures                                     | 签名,通常指交易的数字签名，它是一种数字化的加密方式，用于验证交易的合法性和完整性      |
| Ledger     | Distributed Ledger                             | 分布式账本，它是一种基于区块链技术的分散式数据库，用于记录和存储所有交易信息         |
| HD         | Hierarchical Deterministic Key                 | 分层确定性密钥，创建多个子钱包                                |
| Sequence   | Sequence                                       | 交易的序列号                                         |
| chainid    | Chain Identifier                               | 链标识符或链身份标识                                     |
| Protobuf   | Protocol Buffers                               | 协议缓冲区，语言无关、平台无关、可扩展的序列化数据结构和协议的方法，用于数据交换、存储和通信 |
| RLP        | Recursive Length Prefix                        | 递归长度前缀，RLP是一种用于编码任意复杂度的数据结构的序列化方法              |
| Mnemonic   | Mnemonic                                       | 助记词                                            |
| denom      | denomination                                   | 即代币或数字资产的单位或面值                                 |
| btf        | byzantine fault tolerance                      | 拜占庭容错共识协议                                      |
| AccAddress | Account Address                                | 账户地址                                           |
| Bech32     | Base32 Encoded Checksum Extended Double-SHA256 | 地址编码格式                                         |

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

## 根据events查询交易

```shell
evmosd  query txs \
--events transfer.sender=evmos1x6cx9236nrsgkyea483nxjtquwdp8u6ru06c8p
```
##  根据hash查询交易
```shell
D799294FE14DB8184605F4B0E5177C8606711812891E175998DC47C57C78DA21
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

## 存储为变量

```shell
export alice=$(checkersd keys show alice -a) $ export bob=$(checkersd keys show bob -a)
```

##  模拟执行
```shell
checkersd tx checkers create-game $alice $bob --from $alice --dry-run

```

##  对base64解码
```shell
echo YWN0aW9u | base64 -d
```