# helm

<!-- TOC -->
* [helm](#helm)
  * [仓库](#仓库)
    * [查看](#查看)
    * [添加](#添加)
    * [更新](#更新)
    * [删除](#删除)
  * [包](#包)
    * [拉取](#拉取)
    * [查看](#查看-1)
    * [创建](#创建)
    * [打包](#打包)
    * [安装](#安装)
    * [卸载](#卸载)
  * [查看实际加载的模板](#查看实际加载的模板)
<!-- TOC -->

## 仓库

### 查看

```shell
helm repo list
```

```shell
helm search hub redis
```

```shell
helm search repo bitnami
```

### 添加

```shell
helm repo add bitnami https://charts.bitnami.com/bitnami

```

### 更新

```shell
helm repo update

```

### 删除

```shell
helm repo remove bitnami

```

## 包
###  拉取
```shell
helm pull bitnami/mysql --version 4.5.2
```
### 查看

```shell
helm ls
```

### 创建

```shell  
helm create zwz-cluster-chart

```

### 打包

```shell  
helm package nginx
```

### 安装

```shell
helm install devlake devlake/devlake --version=0.17.0-beta11 --set service.uiPort=30000

```
```shell
helm install full-coral ./mychart
```
### 卸载

```shell
helm uninstall devlake


```

## 查看实际加载的模板
```shell
helm get manifest full-coral
```
```shell
helm install --debug --dry-run goodly-guppy ./mychart
```