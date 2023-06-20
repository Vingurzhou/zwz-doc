# helm

<!-- TOC -->
* [helm](#helm)
  * [仓库](#仓库)
    * [查看](#查看)
    * [添加](#添加)
    * [更新](#更新)
    * [删除](#删除)
  * [包](#包)
    * [查看](#查看-1)
    * [创建](#创建)
    * [打包](#打包)
    * [安装](#安装)
    * [卸载](#卸载)
<!-- TOC -->

## 仓库

### 查看

```shell
helm repo list

```

### 添加

```shell
helm repo add devlake https://apache.github.io/incubator-devlake-helm-chart

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

### 查看

```shell
helm ls
```

### 创建

```shell  
helm create nginx
```

### 打包

```shell  
helm package nginx
```

### 安装

```shell
helm install devlake devlake/devlake --version=0.17.0-beta11

```

### 卸载

```shell
helm uninstall devlake


```

