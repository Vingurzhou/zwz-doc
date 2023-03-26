# git

<!-- TOC -->

* [git](#git)
    * [.gitattributes](#gitattributes)
    * [commit message](#commit-message)
        * [type(必须)](#type--必须-)
        * [scope(可选)](#scope--可选-)
        * [subject(必须)](#subject--必须-)

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