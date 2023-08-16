# mysql

<!-- TOC -->
* [mysql](#mysql)
  * [术语](#术语)
  * [远程权限](#远程权限)
  * [水平切分](#水平切分)
  * [读写分离](#读写分离)
  * [垂直切分](#垂直切分)
<!-- TOC -->

## 术语

| 缩写           | 全称            | 含义  |
|--------------|---------------|-----|
| derived      | Derived Table | 派生表 |
| alias        | AS            | 别名  |
| incompatible | incompatible  | 不相容 |

## 远程权限

1. 进入mysql库
2. 进入user表
3. 将root用户的host由localhost改成%
4. 刷新数据库缓存
5. 打开服务商安全组端口
6. 打开系统防火墙端口
7. 修改mysql.cnf的bind-address为0.0.0.0
8. 重启mysql

## 水平切分

```shell
分库分表
```

## 读写分离

在常见的读写分离架构中，通常会有一个主数据库（Master）和一个或多个从数据库（Slave）。主数据库负责处理写操作（INSERT、UPDATE、DELETE等），并将数据的变化同步到从数据库。从数据库主要处理读操作（SELECT等），从而分担了主数据库的读负载。

## 垂直切分

```shell
多表连查
```

##  查看正在执行语句
```sql
select * from information_schema.PROCESSLIST where info is not null
```
```sql
-- 1、设置
SET GLOBAL log_output = 'TABLE';  SET GLOBAL general_log = 'ON';
SET GLOBAL log_output = 'TABLE';  SET GLOBAL general_log = 'OFF';

-- 2、查询
SELECT * from mysql.general_log ORDER BY    event_time DESC
```