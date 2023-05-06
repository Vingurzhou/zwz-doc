# golang

<!-- TOC -->
* [golang](#golang)
  * [代码执行命令](#代码执行命令)
  * [重定向标准输入流](#重定向标准输入流)
  * [go环境配置](#go环境配置)
    * [CGO_ENABLED](#cgoenabled)
  * [goland](#goland)
<!-- TOC -->

## 代码执行命令

注意：
linux必须用bash，没加入shell变量必须用绝对路径

```golang
cmd := exec.Command("bash", "-c", fmt.Sprintf("echo 12345678|/opt/go/gopath/bin/tntchaind tx bank send %s %s %s -y", req.From, req.To, req.Amount))
stdout, err := cmd.CombinedOutput()
```

## 重定向标准输入流

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

## go环境配置

### CGO_ENABLED

`CGO_ENABLED=0` 是一个环境变量，用于在编译 Go 代码时控制 CGO 编译器的开关。CGO（C Go）是 Go 语言的一个功能，它允许 Go 代码与
C 代码进行交互。当 CGO_ENABLED 设置为 1 时，Go 编译器将使用 CGO 编译器来编译 C 代码并将其链接到 Go 代码中。而当 CGO_ENABLED
设置为 0 时，Go 编译器将忽略所有的 C 代码，并仅编译 Go 代码。

在很多情况下，CGO 是 Go 语言的一个重要特性，它可以让 Go 代码与底层的 C 代码进行交互，从而获得更高的性能和更多的功能。但是在某些情况下，比如在某些平台或环境下，使用
CGO 可能会导致一些问题。在这种情况下，可以将 CGO_ENABLED 设置为 0，以便完全禁用 CGO。

在上下文中，设置 `CGO_ENABLED=0` 可能是为了避免在编译时链接 C 代码或库，这对于跨平台编译或编译不需要 C 代码的纯 Go 代码特别有用。

##  goland
