## k8s
<!-- TOC -->
  * [k8s](#k8s)
    * [kubernetes-dashboard](#kubernetes-dashboard)
    * [删除命名空间](#删除命名空间)
    * [查看所有](#查看所有)
<!-- TOC -->
### kubernetes-dashboard

```shell
kubectl proxy --port=8001

kubectl -n kubernetes-dashboard create token admin-user

echo http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/

```

### 删除命名空间

```shell
kubectl delete namespace jenkins
```

### 查看所有

```shell
kubectl get all
```
