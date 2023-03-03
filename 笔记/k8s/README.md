## k8s

<!-- TOC -->
  * [k8s](#k8s)
    * [kubernetes-dashboard](#kubernetes-dashboard)
    * [删除资源](#删除资源)
    * [获得资源信息](#获得资源信息)
    * [创建资源](#创建资源)
    * [更新资源](#更新资源)
<!-- TOC -->

### kubernetes-dashboard

```shell
kubectl proxy --port=8001
kubectl -n kubernetes-dashboard create token admin-user
echo http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/

```

### 删除资源

```shell
kubectl delete namespace jenkins
```

### 获得资源信息

```shell
kubectl get all
```

### 创建资源

```shell
kubectl create namespace greet-api
```

### 更新资源
```shell
kubectl apply -f k8s.yaml

```