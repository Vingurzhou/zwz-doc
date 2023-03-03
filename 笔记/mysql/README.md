## mysql

###  设置远程权限
```shell
$ docker exec -it zwoastro-mysql mysql -uroot -p
##输入密码：PXDN93VRKUm8TeE7
use mysql;
update user set host='%' where user='root';
FLUSH PRIVILEGES;

ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'Z00a0319';
FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';
```