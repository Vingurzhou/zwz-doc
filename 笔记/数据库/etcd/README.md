#   etcd
##
```shell
cat ./global_config.yaml | docker-compose exec -T enjoyfood-backend-etcd sh -c "export ETCDCTL_API=3 && etcdctl put /enjoyfood-backend/global_config" && \
```
