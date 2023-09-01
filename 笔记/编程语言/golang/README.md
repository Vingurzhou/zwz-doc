# golang

<!-- TOC -->
* [golang](#golang)
  * [字符](#字符)
    * [比较](#比较)
  * [数值](#数值)
    * [数值转换](#数值转换)
  * [数组](#数组)
    * [for r](#for-r)
    * [多维数组简写](#多维数组简写)
    * [数组、切片互转](#数组切片互转)
  * [编译](#编译)
    * [查看支持哪些平台](#查看支持哪些平台)
    * [cgo交叉编译](#cgo交叉编译)
  * [并发](#并发)
    * [锁(Mutex、RWMutex、WaitGroup)](#锁--mutexrwmutexwaitgroup-)
    * [通道(chan)](#通道--chan-)
    * [无缓冲通道(make(chan int))](#无缓冲通道--make--chan-int--)
  * [其他](#其他)
    * [代码执行命令](#代码执行命令)
    * [重定向标准输入流](#重定向标准输入流)
    * [为什么request.URL.Scheme取不到值](#为什么requesturlscheme取不到值)
    * [捕获错误](#捕获错误)
    * [golang的goprivate参数是做什么的](#golang的goprivate参数是做什么的)
    * [optionalAssets := make([]*pb.Material, 0, len(result.SynthOrder.OptionalAssets))](#optionalassets---make-----pbmaterial-0-len--resultsynthorderoptionalassets--)
    * [cgo交叉编译](#cgo交叉编译-1)
<!-- TOC -->
##术语

| 简称  | 全称                       | 含义          |
|-----|--------------------------|-------------|
| mux | HTTP request multiplexer | HTTP请求多路复用器 |

## 字符

### 比较

uint8和int32不是不能比较嘛，为啥在golang中``'f'``和``"f"[0]``相等

在Go语言中，`'f'`和`"f"[0]`
相等是因为Go语言有一种特殊的数据类型叫做rune（也称为Unicode代码点），它可以用来表示任何Unicode字符。在Go语言中，rune类型默认为int32类型的别名，因此可以和int32类型进行比较。

在Go语言中，`'f'`是一个rune类型的字面量，等价于数字102（表示Unicode代码点U+0066）。`"f"[0]`
是一个字符串类型的字面量，它代表一个长度为1的字符串，其中包含一个字节0x66（即ASCII码表中的字符`'f'`
）。当这两个值进行比较时，Go语言会将字符串类型的字面量自动转换为rune类型，因此它们实际上是相等的。

需要注意的是，虽然rune类型和int32类型在Go语言中可以相互转换，但是在实际使用中，它们并不完全相同。rune类型通常用于表示Unicode字符，而int32类型则用于表示整数值。因此，在比较不同类型的值时，需要仔细考虑它们的含义和数据类型。

## 数值

### 数值转换

对于非常大的数值，浮点数表示法可能会引起精度丢失问题。为了避免这个问题，可以使用Go语言中的`math/big`包来处理大整数。

对于更大的数值，如果直接使用 float64 或 big.Float 进行转换和计算，可能会导致精度问题。在这种情况下，可以使用 Go
语言中的第三方库`github.com/shopspring/decimal` 来处理高精度的十进制数值。

## 数组
### for r
```
for _, v := range arr {
v := v
res = append(res, &v)
}
```

```
for k := range arr {
res = append(res, &arr[k])
}
```
### 多维数组简写

```go
var a [][]int
a := [][]int{{-1, -1, 2}, {-1, 0, 1}}
```

### 数组、切片互转

slice：make分配底层数组，var不分配为nil（map同理）
hashtable的key可以是数组，不可以是切片

```go
slice := []int{1, 2, 3, 4, 5} // 切片

// 将切片转换为数组
array := make([]int, len(slice))
copy(array, slice)

```

```go
array := [5]int{1, 2, 3, 4, 5} // 数组

// 将数组转换为切片
slice := array[:]

```

## 编译

### 查看支持哪些平台

```shell
#go tool dist list
go tool dist list -json | jq -r '.[] | select(.FirstClass) | [.GOOS , .GOARCH] | join("/")'
```

### cgo交叉编译
* GOARCH, 目标平台的 CPU 架构. 常用的值amd64, arm64,i386,armhf
* GOOS, 目标平台, 常用的值 linux, windows, drawin (macOS)
* GOARM, 只有 GOARCH 是 arm64 才有效, 表示 arm 的版本, 只能是 5, 6, 7 其中之一
* CGO_ENABLED, 是否支持 CGO 交叉汇编, 值只能是 0, 1, 默认情况下是 0, 启用交叉汇编比较麻烦
* CC, 当支持交叉汇编时(即 CGO_ENABLED=1), 编译目标文件使用的c 编译器.
* CXX, 当支持交叉汇编时(即 CGO_ENABLED=1), 编译目标文件使用的 c++ 编译器.
* AR, 当支持交叉汇编时(即 CGO_ENABLED=1), 编译目标文件使用的创建库文件命令.

arm 交叉汇编下载地址:
http://releases.linaro.org/components/toolchain/binaries, 选择
目录下的文件作为交叉编译工具.

| tool | armhf		                  | arm64                  | eabi                  |
|------|--------------------------|------------------------|-----------------------|
| gcc  | gcc-arm-linux-gnueabihf	 | gcc-aarch64-linux-gnu	 | gcc-arm-linux-gnueabi |
| g++	 | g++-arm-linux-gnueabihf	 | g++-aarch64-linux-gnu	 | g++-arm-linux-gnueabi |

```shell
GOOS=linux GOARCH=arm64 GOARM=7 CGO_ENABLED=1 CC=aarch64-linux-gnu-gcc AR=aarch64-linux-gnu-ar go build -o ./build/ ./cmd/...
GOOS=linux GOARCH=arm CGO_ENABLED=1 CC=arm-linux-gnueabihf-gcc AR=arm-linux-gnueabihf-ar go build
```

## 并发

### 锁(Mutex、RWMutex、WaitGroup)

* 信号（sync.Cond）是condition
* 互斥锁可以替代读写锁，但是读写锁性能好

### 通道(chan)

* 阻塞main协程会报错

### 无缓冲通道(make(chan int))

* <-channel会阻塞当前协程直到其他协程channel<-struct{}{}
* channel<-struct{}{}会阻塞当前协程直到其他协程<-channel

## 其他

### 代码执行命令

注意：
linux必须用bash，没加入shell变量必须用绝对路径

```golang
cmd := exec.Command("bash", "-c", fmt.Sprintf("echo 12345678|/opt/go/gopath/bin/tntchaind tx bank send %s %s %s -y", req.From, req.To, req.Amount))
stdout, err := cmd.CombinedOutput()
```

### 重定向标准输入流

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

### 为什么request.URL.Scheme取不到值

```go
switch {
case r.TLS == nil:
r.URL.Scheme = "https"
case r.Header.Get("X-Forwarded-Proto") != "":
r.URL.Scheme = r.Header.Get("X-Forwarded-Proto")
case r.Header.Get("X-Forwarded-Protocol") != "":
r.URL.Scheme = r.Header.Get("X-Forwarded-Protocol")
case r.Header.Get("X-Forwarded-Ssl") != "":
r.URL.Scheme = r.Header.Get("X-Forwarded-Ssl")
case r.Header.Get("X-Url-Scheme") != "":
r.URL.Scheme = r.Header.Get("X-Url-Scheme")
default:
r.URL.Scheme = "http"
}
```

### 捕获错误

```go
func run() string {
var answer string
func () {
defer func () {
err := recover()
fmt.Println(err)
}()

for i := 0; i < 4; i++ {
answer += "dafdsafkldkj"
if i == 3 {
panic("error occur")
}
}
}()

return answer
}
```

```go
func run() (answer string) {
defer func () {
err := recover()
fmt.Println(err)
}()

for i := 0; i < 4; i++ {
answer += "dafdsafkldkj"
if i == 3 {
panic("error occur")
}
}

return answer
}

```

### golang的goprivate参数是做什么的

在Go编程语言中，goprivate是一个环境变量或配置参数，用于控制Go命令在获取私有模块时的行为。它是在Go 1.13版本中引入的一个特性。

当您使用Go命令下载或获取依赖的模块时，它会尝试从代理服务器或版本控制系统获取这些模块。goprivate参数允许您指定一个私有模块的模式，以告诉Go命令哪些模块是私有的，不应该通过代理服务器公开获取。

该参数的值是一个模式列表，模式用于匹配私有模块的路径。模式可以包含通配符，以便匹配多个路径。如果Go命令在下载依赖模块时匹配到了这些模式，它将不会使用代理服务器，而是尝试直接从源代码获取私有模块。

```shell
export GOPRIVATE=github.com/astra-x/*,github.com/yuhu-tech/*,github.com/go-redis/*,go.etcd.io/* && \
```

### optionalAssets := make([]*pb.Material, 0, len(result.SynthOrder.OptionalAssets))

只要元素数量保持低于最初指定的容量，您就可以在代码中高效地将元素附加到切片，而无需重新分配内存。

### cgo交叉编译

我们都知道在不涉及 CGO 的时候，Go 的交叉编译非常简单，只需要设置对应的 GOOS 和 GOARCH 即可，但当涉及到 CGO
时，问题就变得有点复杂了，因为你需要指定特定的 GCC。

例如，想在 Ubuntu 上交叉编译一个带有 CGO 的动态库，目标 CPU 架构为 arm，我们该如何操作呢？

示例代码

`shared.gopackage mainimport "C"//export Sumfunc Sum(a, b int) int {return a + b}func main(){}
`
这个代码使用到了 CGO，然后暴露一个 Sum 方法，实现两个整数相加。

编译 32 位的 arm

因为通过设置 CGO_ENABLED=1 开启 CGO 编译，执行命令如下：

CGO_ENABLED=1 GOOS=linux GOARCH=arm go build -buildmode=c-shared -o share.so
但不幸，命令报错： gcc: error: unrecognized command line option '-marm'。

正如一开始我提到，交叉编译 CGO 需要选择特定的 arm 交叉编译工具，而 Ubuntu 上编译 32 位的 arm 可以使用
gcc-arm-linux-gnueabihf，安装命令如下：

sudo apt-get updatesudo apt-get install gcc-arm-linux-gnueabihf
安装完成后，指定 CC 重新编译：

CGO_ENABLED=1 GOOS=linux GOARCH=arm CC=arm-linux-gnueabihf-gcc go build -buildmode=c-shared -o share.so
命令成功运行，此时目录下已经生成了一个叫做 share.so 的文件，通过 file 命令查看其属性，可以确认确实为 arm 32 版本。

share.so: ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, BuildID[sha1]
=7b23579ddcbebdfc8f4b68512859661a45d66996, not stripped
编译 64 位的 arm

交叉编译的时候，不仅要针对平台选择 GCC，而且还要根据操作系统的位数来选，所以 64 位需要选择不同的 GCC，这里推荐
gcc-linaro-5.3-2016.02-x86_64_aarch64-linux-gnu.tar.xz。

安装命令:

wget https://releases.linaro.org/components/toolchain/binaries/5.3-2016.02/aarch64-linux-gnu/gcc-linaro-5.3-2016.02-x86_64_aarch64-linux-gnu.tar.xz
tar xvf gcc-linaro-5.3-2016.02-x86_64_aarch64-linux-gnu.tar.xz -C /usr/lib/echo 'export PATH="$PATH:
/usr/lib/gcc-linaro-5.3-2016.02-x86_64_aarch64-linux-gnu/bin"' >> ~/.bashrcsource ~/.bashrc
安装完成，重新执行编译命令：

CGO_ENABLED=1 GOOS=linux GOARCH=arm64 CC=aarch64-linux-gnu-gcc-5.3.1 go build -buildmode=c-shared -o share.so
编译成功，并产生一个 share.so 文件，同样我们使用 file share.so 查看其元信息为：

share.so: ELF 64-bit LSB shared object, ARM aarch64, version 1 (SYSV), dynamically linked, BuildID[sha1]
=5b0e7ff7c3af178039a7b934df8ca3e7572ab5b5, not stripped
到目前为止，我们已经成功在 Ubuntu 系统上交叉编译出了 CGO 程序的 arm 和 arm64 两个版本。

总结

当 Go 交叉编译涉及到 CGO 时，只指定 GOOS 和 GOARCH 是不够的，还需要通过 CC 参数指定相应的 GCC 版本，而 GCC
的选择又与当前系统以及目标架构有关：

交叉编译目标 CPU 架构(包括 32位 还是 64位)。
交叉编译所在操作系统。