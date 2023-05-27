# mysql

<!-- TOC -->
* [mysql](#mysql)
  * [术语](#术语)
  * [设置远程权限](#设置远程权限)
<!-- TOC -->

## 术语

| 缩写           | 全称            | 含义  |
|--------------|---------------|-----|
| derived      | Derived Table | 派生表 |
| alias        | AS            | 别名  |
| incompatible | incompatible  | 不相容 |
|              |               |     |

## 设置远程权限

1. 进入mysql库
2. 进入user表
3. 将root用户的host由localhost改成%
4. 刷新数据库缓存
5. 打开服务商安全组端口
6. 打开系统防火墙端口
7. 修改mysql.cnf的bind-adress为0.0.0.0
8. 重启mysql