# kafka
<!-- TOC -->
* [kafka](#kafka)
  * [创建topic](#创建topic)
<!-- TOC -->
## 创建topic

```shell
$ docker exec -it kafka /bin/sh
$ cd /opt/kafka/bin/
$ kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
```