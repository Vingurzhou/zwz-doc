# golang

<!-- TOC -->
* [golang](#golang)
  * [执行命令](#执行命令)
  * [重定向标准输入流](#重定向标准输入流)
<!-- TOC -->

## 执行命令

注意：
linux必须用bash，没加入shell变量必须用绝对路径

```golang
cmd := exec.Command("bash", "-c", fmt.Sprintf("echo 12345678|/opt/go/gopath/bin/tntchaind tx bank send %s %s %s -y", req.From, req.To, req.Amount))
stdout, err := cmd.CombinedOutput()
```
##  重定向标准输入流
我在这段函数前执行哪些golang代码，才能运行下面这个代码时得到false
```golang
func inputIsTty() bool {
return isatty.IsTerminal(os.Stdin.Fd()) || isatty.IsCygwinTerminal(os.Stdin.Fd())
}

```
```golang
package main

import (
	"os"
)

func main() {
	// 重定向标准输入流
	file, err := os.Open("/dev/null")
	if err != nil {
		panic(err)
	}
	defer file.Close()
	os.Stdin = file
}
```