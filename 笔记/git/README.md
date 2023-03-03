## git
<!-- TOC -->
  * [git](#git)
    * [.gitattributes](#gitattributes)
<!-- TOC -->
### .gitattributes
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
