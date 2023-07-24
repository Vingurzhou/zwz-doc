# git

<!-- TOC -->
* [git](#git)
  * [.gitattributes](#gitattributes)
  * [commit message](#commit-message)
    * [type(必须)](#type--必须-)
    * [scope(可选)](#scope--可选-)
    * [subject(必须)](#subject--必须-)
  * [创建ssh密钥](#创建ssh密钥)
  * [配置 SSH 代理](#配置-ssh-代理)
  * [验证](#验证)
  * [克隆某个分支或某个tag](#克隆某个分支或某个tag)
  * [查看配置](#查看配置)
  * [删除用户名和邮箱](#删除用户名和邮箱)
  * [设置http头](#设置http头)
  * [创建远程仓库](#创建远程仓库)
  * [添加远程分支](#添加远程分支)
  * [查看本地和远程分支](#查看本地和远程分支)
  * [切换分支](#切换分支)
  * [创建本地和远程分支](#创建本地和远程分支)
  * [删除本地和远程分支](#删除本地和远程分支)
  * [下载远程](#下载远程)
  * [被其他分支合并](#被其他分支合并)
  * [取消远程仓库](#取消远程仓库)
  * [重置](#重置)
  * [查看配置](#查看配置-1)
  * [修改通信协议](#修改通信协议)
  * [代理](#代理)
  * [设置postbuffer](#设置postbuffer)
  * [创建分支，线上pr](#创建分支线上pr)
  * [回滚到上一个commit](#回滚到上一个commit)
  * [延用上一个commit](#延用上一个commit)
<!-- TOC -->

## .gitattributes

您可以使用GitHub仓库中的.gitattributes文件来指定要显示或隐藏的文件类型。这个文件的作用是告诉Git如何处理某些文件。

如果您想要隐藏某种类型的文件，您可以在.gitattributes文件中添加以下内容：

`*.extension linguist-vendored`

其中extension是您想要隐藏的文件类型的扩展名。例如，如果您想要隐藏所有.txt文件，您可以将上述行改为：

`*.txt linguist-vendored`

如果您想要显示某种类型的文件，您可以在.gitattributes文件中添加以下内容：

`*.extension linguist-detectable`

同样地，extension是您想要显示的文件类型的扩展名。例如，如果您想要显示所有.md文件，您可以将上述行改为：

`*.md linguist-detectable`

请注意，这些更改不会立即生效，而是需要提交并推送到GitHub仓库才能生效。

## commit message

```
<type>(<scope>): <subject>
```

### type(必须)

用于说明git commit的类别，只允许使用下面的标识。

* feat：新功能（feature）。
* fix/to：修复bug，可以是QA发现的BUG，也可以是研发自己发现的BUG。
* fix：产生diff并自动修复此问题。适合于一次提交直接修复问题
* to：只产生diff不自动修复此问题。适合于多次提交。最终修复问题提交时使用fix
* docs：文档（documentation）。
* style：格式（不影响代码运行的变动）。
* refactor：重构（即不是新增功能，也不是修改bug的代码变动）。
* perf：优化相关，比如提升性能、体验。
* test：增加测试。
* chore：构建过程或辅助工具的变动。
* revert：回滚到上一个版本。
* merge：代码合并。
* sync：同步主线或分支的Bug。

### scope(可选)

scope用于说明 commit 影响的范围，比如数据层、控制层、视图层等等，视项目不同而不同。

例如在Angular，可以是:

* location
* browser
* compile
* compile
* rootScope
* ngHref
* ngClick
* ngView

如果你的修改影响了不止一个scope，你可以使用*代替。

### subject(必须)

subject是commit目的的简短描述，不超过50个字符。
结尾不加句号或其他标点符号。

根据以上规范git commit message将是如下的格式：

```
fix(DAO):用户查询缺少username属性
feat(Controller):用户查询接口开发
```
##  创建ssh密钥
```shell
ssh-keygen -t ed25519 -C "zwz0123460218@icloud.com"

```
##  配置 SSH 代理
```shell
open ~/.ssh/config
```
```shell
# 第一个 GitHub 账号
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519

# 第二个 GitHub 账号
Host github-second
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_second

```
##  验证
```shell
ssh -T git@github-second
```
##  克隆某个分支或某个tag
```shell
#git clone --single-branch <仓库URL> -b <分支名>
git clone --branch v12.1.5 \
--single-branch https://github.com/evmos/evmos.git \
/Users/zhouwenzhe/src/youyaProject/evmos

```
## 查看配置

```shell
git config --list

```
##  删除用户名和邮箱
```shell
git config --global --unset user.name
git config --global --unset user.email
```
##  设置http头
```shell
git config --global http.extraheader "Authorization: Basic Y2hlbnFpbmcteXVodTo2YWNiOGU0YjFjZThiZmYxMTM1ODkwY2RkZWJhNWE0YjcxNGRlNzE2" && \
git config --global https.extraheader "Authorization: Basic Y2hlbnFpbmcteXVodTo2YWNiOGU0YjFjZThiZmYxMTM1ODkwY2RkZWJhNWE0YjcxNGRlNzE2" && \

```
## 创建远程仓库

```shell
git init 
```

## 添加远程分支

```shell
git remote add origin https://github.com/Vingurzhou/zwz-doc.git
```

## 查看本地和远程分支

```shell
git remote prune origin
git remote -v
git branch -a
```

## 切换分支

```shell
git checkout main
```

## 创建本地和远程分支

```shell
git branch test
git push -u origin test
```

## 删除本地和远程分支

```shell
git branch -d test2
git push origin --delete test2
```

## 下载远程
```shell
git fetch

```
```shell
git pull
```
##  用远程分支强制覆盖当前分支
```shell
git reset --hard origin/zwz_2023_0724_feat_assets_cron

```
## 被其他分支合并

```shell
git merge 
```

## 取消远程仓库

```shell
rm -rf .git
```
##  重置
```shell
git config --global --edit
```
## 查看配置
```shell
git config --global --list
```
## 修改通信协议
```shell
git config --global http.version HTTP/1.1
```
##  代理
```shell
git config --global https.proxy 'socks5://127.0.0.1:3213'
```
##  设置postbuffer
```shell
git config --global http.postBuffer 524288000

```
##  创建分支，线上pr
```shell
git push origin devel-v10.4.0:zwz_2023_0719_feat_assets_service
```

##  回滚到上一个commit
```shell
git reset --soft head^1
```
##  延用上一个commit
```shell
 git commit --amend  
```
##  合并两个commit
```shell
 git rebase -i 6043b09f8173d51dbb0bdbea0c897d99e0810094
```
##  撤销rebase
````shell
git rebase --abort
````