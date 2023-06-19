# goctl

<!-- TOC -->
* [goctl](#goctl)
  * [api](#api)
  * [model](#model)
  * [swagger](#swagger)
<!-- TOC -->

## api

```shell
goctl api go -api "./cmd/api/*.api" -dir "./cmd/api" --style=gozero --home="../../deploy/goctl/1.3.4" --style=gozero
```

## model

```shell
goctl model mysql datasource -url="root:Z00a0319@tcp(127.0.0.1)/zwzmicro_shop" -table="*" -dir="./model" -cache=true --style=gozero --home="../../deploy/goctl/1.3.4"
```

## swagger

```shell
goctl api plugin -plugin goctl-swagger="swagger -filename swagger.json" -api ./cmd/desc/api/*.api -dir "./"

```