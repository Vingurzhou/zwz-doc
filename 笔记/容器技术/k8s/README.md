# k8s

<!-- TOC -->
* [k8s](#k8s)
  * [术语](#术语)
  * [kubeadm](#kubeadm)
    * [初始化集群](#初始化集群)
    * [生成新token](#生成新token)
    * [加入集群](#加入集群)
  * [kubectl](#kubectl)
    * [应用资源](#应用资源)
    * [删除资源](#删除资源)
    * [查看资源](#查看资源)
    * [查看日志](#查看日志)
    * [node](#node)
      * [查看](#查看)
      * [加标签](#加标签)
    * [namespaces](#namespaces)
      * [查看](#查看-1)
    * [configmap](#configmap)
      * [查看](#查看-2)
      * [描述](#描述)
    * [pod](#pod)
      * [查看](#查看-3)
      * [描述](#描述-1)
      * [进入](#进入)
      * [转发](#转发)
    * [job](#job)
      * [查看](#查看-4)
    * [service](#service)
      * [查看](#查看-5)
    * [deployment](#deployment)
      * [查看](#查看-6)
<!-- TOC -->

## 术语

| 缩写          | 全称                                    | 含义                                                                   |
|-------------|---------------------------------------|----------------------------------------------------------------------|
| node        | node                                  | Kubernetes 集群中的一台机器，这台机器可以是物理机或者是虚拟机                                 |
| pod         | pod                                   | 源自鲸鱼的群体（一群鲸鱼被称为一个"pod"）                                              |
| master      | Master Node                           | 集群中的管理节点，运行着控制和协调整个集群的软件组件，如 kube-apiserver、kube-scheduler 和 etcd 等。 |
| worker      | Worker Node                           | 集群中的工作节点，运行着应用程序的容器                                                  |
| metadata    | metadata                              | 描述和管理Kubernetes对象的元数据信息                                              |
| spec        | specification                         | 定义对象的规范或配置                                                           |
| policy      | policy                                | 控制和管理Kubernetes资源的规则或策略                                              |
| immutable   | immutable                             | 不可变                                                                  |
| Manifest    | Manifest                              | 清单                                                                   |
| completions | Job Completions                       | 定义Job资源中的完成数目                                                        |
| Probe       | Probe                                 | 探针                                                                   |
| Affinity    | Affinity                              | 亲和性                                                                  |
| Schedule    | Scheduling                            | 调度                                                                   |
| Operator    | Operator                              | 实现自动化管理的软件模式或模式框架                                                    |
| disktype    | disktype                              | 磁盘的类型                                                                |
| HDD         | Hard Disk Drive                       | 硬盘驱动器，传统的机械磁盘                                                        |
| SSD         | Solid State Drive                     | 固态硬盘                                                                 |
| NVMe        | Non-Volatile Memory Express           | 一种高性能的存储接口和协议，用于连接固态硬盘（SSD）到计算机系统，提供更低的延迟和更高的数据传输速度                  |
| SATA        | Serial Advanced Technology Attachment | 一种用于连接硬盘驱动器到计算机系统的接口标准，常用于连接传统硬盘驱动器（HDD）和一些固态硬盘（SSD）。                |
| SAS         | Serial Attached SCSI                  | 一种用于连接高性能硬盘驱动器和其他外部设备的接口标准，常用于连接企业级硬盘驱动器和存储系统                        |
| assign      | assign                                | 分配                                                                   |
| privileged  | privileged                            | 特权                                                                   |
| escalation  | escalation                            | 升级                                                                   |
| Ingress     | Ingress                               | 入口                                                                   |
| replicas    | replicas                              | 副本集                                                                  |
| ep          | endpoints                             | 端点                                                                   |

## kubeadm

### 初始化集群

```shell
kubeadm init --apiserver-advertise-address=0.0.0.0 \
--apiserver-cert-extra-sans=127.0.0.1 \
--image-repository=registry.aliyuncs.com/google_containers \
--ignore-preflight-errors=all \
--kubernetes-version=v1.27.3 \
--service-cidr=10.10.0.0/16 \
--pod-network-cidr=10.18.0.0/16

```

### 生成新token

```shell
kubeadm token create --print-join-command
```

### 加入集群

```shell
kubeadm join 192.168.99.101:6443 --token vldjakslfjdksjlaf 
```

## kubectl

### 应用资源

```shell
kubectl apply -f recommended.yaml

```

### 删除资源

```shell
kubectl delete -f test.yaml
```

### 查看资源

```shell
kubectl --kubeconfig=/Users/zhouwenzhe/src/zwz-doc/笔记/容器技术/k8s/wlb965.kube.conf get deployment,svc,pods,ingress -o wide 
```

### 查看日志

```shell
kubectl logs zwz-admin
```

### node

#### 查看

```shell
kubectl get nodes --show-labels -o wide

``` 

#### 加标签

```shell
kubectl label nodes node2 disktype=ssd

```

### namespaces

#### 查看

```shell
kubectl get namespaces
```

### configmap

#### 查看

```shell 
kubectl get configmap -n kube-system
```

#### 描述

```shell
kubectl describe configmap kubeadm-config -n kube-system
```

### pod

#### 查看

```shell
kubectl get pod --all-namespaces -w -o wide

```

```shell
kubectl get pod kube-apiserver-docker-desktop -n kube-system -o yaml 

```

#### 描述

```shell
kubectl describe pod kube-apiserver-docker-desktop -n kube-system 
```

#### 进入

```shell
kubectl exec -it zwz-admin sh

```
#### 转发
将网络流量从本地计算机转发到 Kubernetes 集群中运行的 pod 上的端口，反之亦然。这对于调试或访问集群中运行的服务非常有用
```shell
kubectl --kubeconfig=/Users/zhouwenzhe/src/zwz-doc/笔记/容器技术/k8s/wlb965.kube.conf port-forward service/wlb965-mysql 3306:3306
```
### job

#### 查看

```shell
kubectl get job 
```

### service

#### 查看

```shell
kubectl get svc
```

### deployment

#### 查看

```shell
kubectl get all
```

