FROM ubuntu:latest
#安装时区
RUN apt-get update && apt-get install -y tzdata
RUN unlink /etc/localtime
#链接宿主机时区到容器内
RUN ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

COPY . /usr/local/bin

CMD ["sh"]