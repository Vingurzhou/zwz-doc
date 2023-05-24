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

##  比较

uint8和int32不是不能比较嘛，为啥在golang中``'f'``和``"f"[0]``相等

在Go语言中，`'f'`和`"f"[0]`
相等是因为Go语言有一种特殊的数据类型叫做rune（也称为Unicode代码点），它可以用来表示任何Unicode字符。在Go语言中，rune类型默认为int32类型的别名，因此可以和int32类型进行比较。

在Go语言中，`'f'`是一个rune类型的字面量，等价于数字102（表示Unicode代码点U+0066）。`"f"[0]`
是一个字符串类型的字面量，它代表一个长度为1的字符串，其中包含一个字节0x66（即ASCII码表中的字符`'f'`
）。当这两个值进行比较时，Go语言会将字符串类型的字面量自动转换为rune类型，因此它们实际上是相等的。

需要注意的是，虽然rune类型和int32类型在Go语言中可以相互转换，但是在实际使用中，它们并不完全相同。rune类型通常用于表示Unicode字符，而int32类型则用于表示整数值。因此，在比较不同类型的值时，需要仔细考虑它们的含义和数据类型。

##  数值转换

对于非常大的数值，浮点数表示法可能会引起精度丢失问题。为了避免这个问题，可以使用Go语言中的`math/big`包来处理大整数。

对于更大的数值，如果直接使用 float64 或 big.Float 进行转换和计算，可能会导致精度问题。在这种情况下，可以使用 Go 语言中的第三方库`github.com/shopspring/decimal` 来处理高精度的十进制数值。

##  捕获错误
```go
func run() string {
	var answer string
	func() {
		defer func() {
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
defer func() {
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
##  多维数组简写
```go
var a [][]int
a:=[][]int{{-1, -1, 2}, {-1, 0, 1}}
```
##  数组、切片互转
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

##  并发
### 锁(Mutex、RWMutex、WaitGroup)
* 信号（sync.Cond）是condition
* 互斥锁可以替代读写锁，但是读写锁性能好
### 通道(chan)
* 阻塞main协程会报错
### 无缓冲通道(make(chan int))
* <-channel会阻塞当前协程直到其他协程channel<-struct{}{}
* channel<-struct{}{}会阻塞当前协程直到其他协程<-channel
### 
