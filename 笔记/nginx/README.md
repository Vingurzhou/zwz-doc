# nginx

<!-- TOC -->
* [nginx](#nginx)
  * [反向代理](#反向代理)
  * [域名](#域名)
  * [日志](#日志)
<!-- TOC -->

## 反向代理

```nginx configuration
      location ~* ^/from/(you|me) {
         proxy_set_header Host $http_host;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header REMOTE-HOST $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_pass http://localhost:1001;
      }

```

## 域名

```nginx configuration
    listen       80;
    server_name  api.zwobt.dev.com;

```

## 日志

```nginx configuration
    error_log  /var/log/nginx/api-zwobt-log.error.log;
    access_log /var/log/nginx/api-zwobt-log.access.log;

```