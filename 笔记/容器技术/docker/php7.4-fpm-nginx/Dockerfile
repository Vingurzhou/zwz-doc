# 选择基础镜像
FROM php:7.4-fpm

# 安装必要的 PHP 扩展
RUN docker-php-ext-install mysqli pdo pdo_mysql

# 选择基础 Nginx 镜像并配置
FROM nginx:latest

# 删除默认配置
RUN rm /etc/nginx/conf.d/default.conf

# 添加我们的配置
ADD nginx.conf /etc/nginx/conf.d/

# 将我们的应用代码复制到容器中
COPY . /var/www/html

# 对外暴露 80 端口
EXPOSE 80
