# 面试题

<!-- TOC -->
* [面试题](#面试题)
  * [go](#go)
    * [协程内存](#协程内存)
    * [为什么叫GO111MODULE](#为什么叫go111module)
    * [gmp](#gmp)
    * [channel状态](#channel状态)
    * [结构体比较](#结构体比较)
    * [make和new区别](#make和new区别)
    * [时间函数增加一天](#时间函数增加一天)
    * [goroutine内跑goroutine](#goroutine内跑goroutine)
    * [判断错误类型](#判断错误类型)
    * [recover](#recover)
    * [控制goroutine关闭](#控制goroutine关闭)
    * [map要注意什么](#map要注意什么)
    * [数组和切片区别](#数组和切片区别)
    * [golang中的对象池](#golang中的对象池)
    * [golang是怎么控制抢占式调度的](#golang是怎么控制抢占式调度的)
  * [redis](#redis)
    * [持久化](#持久化)
    * [集群](#集群)
    * [哨兵](#哨兵)
  * [linux](#linux)
    * [linux bridge](#linux-bridge)
    * [proc目录内是什么](#proc目录内是什么)
  * [网络协议](#网络协议)
    * [HTTP（Hypertext Transfer Protocol）](#httphypertext-transfer-protocol)
    * [HTTPS（HTTP Secure）](#httpshttp-secure)
    * [FTP（File Transfer Protocol）](#ftpfile-transfer-protocol)
    * [SMTP（Simple Mail Transfer Protocol）](#smtpsimple-mail-transfer-protocol)
    * [POP3（Post Office Protocol version 3）](#pop3post-office-protocol-version-3)
    * [IMAP（Internet Message Access Protocol）](#imapinternet-message-access-protocol)
    * [DNS（Domain Name System）](#dnsdomain-name-system)
    * [TCP（Transmission Control Protocol）](#tcptransmission-control-protocol)
    * [UDP（User Datagram Protocol）](#udpuser-datagram-protocol)
    * [ICMP（Internet Control Message Protocol）](#icmpinternet-control-message-protocol)
    * [IP（Internet Protocol）](#ipinternet-protocol)
<!-- TOC -->

## go

### 协程内存

每个协程至少需要消耗2KB 的空间，那么假设计算机的内存是2GB，那么至多允许2GB/2KB = 1M 个协程同时存在。 一个Goroutine消耗多少CPU
实际上跟执行函数的逻辑有着很大的关系，如果执行的函数是CPU密集型的计算，并且持续的时间很长，那么这个时候CPU就会优先到达瓶颈。

### 为什么叫GO111MODULE

GO111MODULE 的命名中的“111”并不是版本号或者日期，而是环境变量的名称。这个命名方式是因为在 Go 语言的历史中，之前使用的
GOPATH 依赖管理方式是基于环境变量的，而 Go 语言在版本 1.11 中引入了模块化管理依赖的机制，所以 GO111MODULE 的名称中包含了“111”。

此外，值得注意的是，GO111MODULE 这个环境变量并不是 Go 语言本身的一部分，而是与 Go 模块机制相关的工具链和构建系统中的一部分。

### gmp

* G（Goroutine）：即Go协程，每个go关键字都会创建一个协程。
* M（Machine）：工作线程，在Go中称为Machine，数量对应真实的CPU数（真正干活的对象）。
* P（Processor）：处理器（Go中定义的一个摡念，非CPU），包含运行Go代码的必要资源，用来调度 G 和 M 之间的关联关系，其数量可通过
  GOMAXPROCS() 来设置，默认为核心数。

M必须拥有P才可以执行G中的代码，P含有一个包含多个G的队列，P可以调度G交由M执行。

### channel状态

Channel是异步进行的, channel存在3种状态：

| 操作   | nil（未初始化的状态，只进行了声明，或者手动赋值为nil） | closed（千万不要误认为关闭channel后，channel的值是nil） | active（正常的channel，可读或者可写） |
|------|--------------------------------|-----------------------------------------|---------------------------|
| 关闭   | 	产生恐慌                          | 	产生恐慌                                   | 	成功关闭                     |
| 发送数据 | 	永久阻塞                          | 	产生恐慌                                   | 	阻塞或者成功发送                 |
| 接收数据 | 	永久阻塞                          | 	永不阻塞                                   | 	阻塞或者成功接收                 |

### 结构体比较

因为是强类型语言，所以不同类型的结构不能作比较，但是同一类型的实例值是可以比较的，实例不可以比较，因为是指针类型

| 结构体类型 | 结构体字段key | 结构体字段value | 字段value类型 | ==比较           | reflect.DeepEqual |
|-------|----------|------------|-----------|----------------|-------------------|
| 相同    | 相同       | 相同         | 字符串       | 相同             |                   |
| 相同    | 相同       | 相同         | 指针        | 不同             |                   |
| 相同    | 相同       | 相同         | 切片        | 报错             | 相同                |
| 不同    | 相同       | 相同         | 字符串       | v1==Value1(v2) |                   |

当其基本类型包含：slice、map、function 时，是不能比较的。若强行比较，就会导致出现例子中的直接报错的情况。

而指针引用，其虽然都是 new(string)，从表象来看是一个东西，但其具体返回的地址是不一样的。

例子中所用到的反射比较方法 reflect.DeepEqual 常用于判定两个值是否深度一致，其规则如下：

* 相同类型的值是深度相等的，不同类型的值永远不会深度相等。
* 当数组值（array）的对应元素深度相等时，数组值是深度相等的。
* 当结构体（struct）值如果其对应的字段（包括导出和未导出的字段）都是深度相等的，则该值是深度相等的。
* 当函数（func）值如果都是零，则是深度相等；否则就不是深度相等。
* 当接口（interface）值如果持有深度相等的具体值，则深度相等。
* [...](http://golang.org/pkg/reflect/#DeepEqual)

### make和new区别

|      | 支持类型           | 返回               | 内存空间 |
|------|----------------|------------------|------|
| make | slice、map、chan | 类型本身 （引用）        | 初始化  |
| new  | 任意类型           | 类型内存地址的指针（*Type） | 清零   |

### 时间函数增加一天

`time.Now().AddDate(0, 0, 1)`

### goroutine内跑goroutine

不会结束

### 判断错误类型

在Golang中，可以使用类型断言（type assertion）来判断一个错误的类型。具体来说，可以使用断言将错误转换为具体的错误类型，然后检查其特定的属性或方法是否存在。

```go
err := doSomething()
if netErr, ok := err.(net.Error); ok {
// err 是一个 net.Error
// 可以通过 netErr 的方法和属性来处理错误
} else {
// err 不是一个 net.Error
// 可以使用其他方式处理错误
}

```

### recover

在一个 defer 延迟执行的函数中调用 recover ，它便能捕捉/中断 panic。

```go
// 错误的 recover 调用示例
func main() {
recover()         // 什么都不会捕捉
panic("not good") // 发生 panic，主程序退出
recover() // 不会被执行
println("ok")
}

// 正确的 recover 调用示例
func main() {
defer func () {
fmt.Println("recovered: ", recover())
}()
panic("not good")
}
```

### 控制goroutine关闭

```go
package main

import (
	"context"
	"fmt"
	"time"
)

func worker(ctx context.Context, id int) {
	for {
		select {
		case <-ctx.Done():
			fmt.Printf("worker %d cancelled\n", id)
			return
		default:
			fmt.Printf("worker %d is running\n", id)
			time.Sleep(time.Second)
		}
	}
}

func main() {
	ctx, cancel := context.WithCancel(context.Background())

	for i := 0; i < 3; i++ {
		go worker(ctx, i)
	}

	time.Sleep(5 * time.Second)
	cancel()
	time.Sleep(time.Second)
	fmt.Println("main goroutine exits")
}

```

在这个例子中，我们创建了一个 context.Context 对象和一个取消函数 cancel。然后启动了三个 worker Goroutine，每个 Goroutine
都在一个无限循环中运行，每秒钟打印一次自己的编号。在每次循环开始时，我们使用 select 语句监控 ctx.Done() channel
是否被关闭，如果被关闭，说明我们需要取消这个 Goroutine。

在 main() 函数中，我们让主 Goroutine 睡眠了 5 秒，然后调用 cancel() 函数，这将关闭 ctx.Done() channel。随着每个 worker
Goroutine 检测到 channel 被关闭，它将退出循环并结束运行。在所有 worker Goroutine 都退出后，主 Goroutine
才会继续运行并打印 "main goroutine exits"。

### map要注意什么

在使用Go语言的map时，需要注意以下几点：

* 并发读写问题：在多个goroutine同时对同一个map进行读写操作时，可能会发生并发冲突，导致程序出现错误。可以使用互斥锁等同步机制来避免这种情况。
* map的扩容会重新分配内存，导致之前的迭代器失效：在对map进行迭代操作时，如果map的容量不够，会进行扩容操作。这个操作会重新分配内存，并且会导致之前的迭代器失效，因此在迭代时要特别小心。
* map的键类型必须支持相等运算符：map的键必须支持相等运算符（==），因为map内部使用哈希表实现，需要通过键的哈希值来快速查找对应的值。如果键类型不支持相等运算符，那么就无法进行哈希计算，也就无法使用map。
* map的值类型可以是任意类型：map的值可以是任意类型，包括函数、结构体、甚至是map本身。但是，由于map是通过哈希表实现的，因此不能将map作为键类型。
* map的初始值为nil：如果没有初始化一个map，那么它的初始值为nil。因此，在使用map之前，必须先对它进行初始化，否则会出现空指针异常。

### 数组和切片区别

数组和切片都是在编程中用于存储一组元素的数据结构，但是它们之间存在一些重要的区别。

* 内存分配方式：数组在声明时需要指定固定的长度，因此在内存中会一次性分配足够的空间来存储所有元素。而切片则是一个动态的结构，它可以根据需要自动调整长度，因此在内存中只会分配当前需要的空间，而不是所有可能需要的空间。
* 可变性：数组的长度是固定的，一旦声明后就不能更改，因此数组中的元素也是不可变的。而切片是可变的，可以根据需要增加或删除元素。
* 值传递和引用传递：当将数组作为参数传递给函数时，会将整个数组复制一份传递给函数，这意味着数组在函数内部进行修改不会影响到原始数组。而将切片传递给函数时，实际上传递的是一个指向底层数组的指针，因此对切片进行的任何修改都会影响到原始数组。
* 语法：数组和切片的访问方式也有所不同。数组的元素可以通过索引直接访问，例如arr[0]
  表示数组arr的第一个元素。而切片的元素则可以通过切片表达式来访问，例如slice[1:3]表示从第二个元素到第四个元素的切片。

总之，数组和切片都是常见的数据结构，但是它们之间有着不同的特点和适用场景，需要根据实际需要选择使用。
### golang中的对象池
在 Go 中，对象池是一种常用的技术，用于重复使用已经分配的对象，从而避免频繁的内存分配和垃圾回收操作，从而提高程序性能和内存使用效率。

Go 标准库中已经提供了 sync.Pool 对象池，它可以用来缓存和重复使用任何可重复使用的对象。sync.Pool 对象池的使用非常简单，只需要创建一个 sync.Pool 对象，调用它的 Get() 方法获取一个对象，调用 Put() 方法将对象放回池中即可。

下面是一个使用 sync.Pool 对象池的示例代码：
```go
package main

import (
	"fmt"
	"sync"
)

type MyObject struct {
	// 定义对象的属性
}

func main() {
	// 创建对象池
	pool := &sync.Pool{
		New: func() interface{} {
			// 创建新对象
			return &MyObject{}
		},
	}

	// 从对象池中获取对象
	obj := pool.Get().(*MyObject)

	// 对对象进行操作
	obj.SomeMethod()

	// 将对象放回对象池中
	pool.Put(obj)

	// 再次从对象池中获取对象，可以看到是同一个对象
	obj = pool.Get().(*MyObject)
	fmt.Println(obj)
}
```
在上面的示例代码中，我们首先定义了一个 MyObject 类型，它表示要重复使用的对象。然后创建了一个 sync.Pool 对象池，使用 New 函数指定了创建新对象的函数。接着使用 Get() 方法从对象池中获取一个 MyObject 对象，并对它进行操作。最后使用 Put() 方法将对象放回池中。我们还演示了从对象池中获取同一个对象的操作。

您可能指的是对象池中使用的对象数组和普通的对象数组之间的区别。

在对象池中，对象数组被用来存储已经创建好的对象，以便在需要时快速地获取和重复使用这些对象。这种技术可以避免频繁地创建和销毁对象，从而提高程序的性能和效率。

与普通的对象数组不同，对象池中的对象数组通常是预先分配好的，其大小固定，因此可以提高程序的内存利用率。当对象不再需要时，它们不会被立即销毁，而是放回对象池中等待下一次使用。这样可以避免频繁地进行内存分配和释放操作，减少程序的内存开销和垃圾回收开销。

另外，对象池中的对象数组通常是线程安全的，这意味着多个 goroutine 可以同时访问和修改这些对象，而不会产生竞态条件和数据竞争问题。这是因为对象池通常会使用锁或其他同步机制来保证对对象数组的访问是线程安全的。

总之，对象池中的对象数组是一种优化技术，用于重复使用已经创建好的对象，以提高程序的性能和效率。与普通的对象数组相比，它们通常具有固定的大小、线程安全性和内存利用率等优点。

### golang是怎么控制抢占式调度的
在 Golang 中，抢占式调度是通过 Go 运行时系统实现的。Go 运行时系统是一个轻量级的并发系统，它有自己的调度器，可以管理和调度所有的 Go 协程。

Go 运行时系统中的调度器使用的是 M:N 线程模型，即把 M 个 Go 协程调度到 N 个操作系统线程上运行。Go 运行时系统会维护一个全局的运行队列（run queue），所有可运行的协程都会加入到这个运行队列中等待被调度。

调度器会周期性地检查所有的操作系统线程和运行队列，如果发现某个协程需要运行，就会将它从运行队列中取出，分配到某个操作系统线程上运行。当协程被分配到线程上后，它会一直运行直到主动让出 CPU 或者被其它协程抢占。

在 Golang 中，协程可以通过调用 runtime.Gosched() 函数来显式地让出 CPU。调度器也会根据一些策略（如时间片轮转）来决定何时抢占某个协程，将 CPU 分配给其它协程运行。因此，Golang 中的抢占式调度是由运行时系统中的调度器实现的。

## redis

### 持久化

| Redis DataBase                      | Append-Only File                    |
|-------------------------------------|-------------------------------------|
| 指定的时间间隔内对Redis的内存数据进行快照，然后将快照保存到磁盘上 | 将每个写操作都记录到一个日志文件中，以便在Redis重新启动时进行恢复 |

### 集群

### 哨兵

## linux

### linux bridge

可以的，Linux Bridge 是 Linux 内核中的一种软件组件，它可以创建虚拟网络桥接器。网络桥接器可以将两个或多个网络段或接口连接起来，使它们能够作为一个单一的网络运行。在
Linux 中，桥接器被创建为一个虚拟设备，系统将其视为物理网络设备。

Linux Bridge 在虚拟化环境中常用于将虚拟机连接到物理网络或彼此连接，以及提供网络隔离和安全性。它也可以用于其他网络场景，例如连接数据中心网络的不同部分。

Linux Bridge 在 OSI 模型的数据链路层（第二层）上运行，执行透明转发帧以及维护转发数据库，将 MAC 地址映射到物理端口，从而使其能够将帧转发到正确的目标。

可以使用 "brctl" 命令行实用程序配置 Linux Bridge，该实用程序允许管理员创建、修改和删除桥接器接口，并将网络接口添加到它们中或从其中删除。此外，许多
Linux 发行版都配备了网络配置工具，提供了用于配置桥接器和其他网络设置的图形界面。

### proc目录内是什么

在Linux系统中，/proc是一个特殊的文件系统，它不包含普通文件，而是包含一些虚拟文件（也称为伪文件），这些文件提供了关于系统内核和进程的信息。

/proc文件系统可以用来查看和修改内核参数、了解系统硬件信息、监控系统性能、查看进程和线程信息等。

下面是/proc目录中常见的一些文件和目录：

* /proc/cpuinfo：包含有关CPU的信息，例如CPU型号、时钟速度、缓存大小等；
* /proc/meminfo：包含有关系统内存使用情况的信息，例如可用内存、缓存和交换空间的大小等；
* /proc/filesystems：列出当前系统支持的文件系统类型；
* /proc/mounts：列出当前已挂载的文件系统；
* /proc/net：包含有关网络协议和统计信息的目录；
* /proc/sys：包含内核参数和系统配置的目录；
* /proc/<pid>/：包含有关指定进程的信息，例如进程状态、打开的文件、内存映射等。其中<pid>为进程的ID。

需要注意的是，/proc目录中的文件和目录都是虚拟的，并不占用实际的存储空间，它们只是在内存中表示系统状态和信息。因此，尝试修改/proc目录中的文件通常是无效的。

## 网络协议

### HTTP（Hypertext Transfer Protocol）

用于在 Web 浏览器和 Web 服务器之间传输数据的协议，常用于访问网页和下载文件。

### HTTPS（HTTP Secure）

HTTP 的加密版本，通过 SSL 或 TLS 加密保护数据传输的安全性。

### FTP（File Transfer Protocol）

用于在网络上传输文件的协议，常用于上传和下载文件。

### SMTP（Simple Mail Transfer Protocol）

用于在邮件服务器之间传输电子邮件的协议，常用于发送和接收邮件。

### POP3（Post Office Protocol version 3）

用于从邮件服务器上下载电子邮件的协议。

### IMAP（Internet Message Access Protocol）

与 POP3 类似，也是用于接收邮件的协议，但它允许在服务器上保留邮件的副本，可以在多个设备上同步邮件。

### DNS（Domain Name System）

用于将域名转换为 IP 地址的协议，使得用户可以通过易于记忆的域名访问网站。

### TCP（Transmission Control Protocol）

一种可靠的传输协议，用于在网络上可靠地传输数据，确保数据包的传输顺序和完整性。

### UDP（User Datagram Protocol）

一种无连接的传输协议，用于在网络上快速传输数据，但不保证数据包的顺序和完整性。

### ICMP（Internet Control Message Protocol）

用于在网络上传输错误消息和状态信息的协议，常用于网络故障排除和诊断。

### IP（Internet Protocol）

它负责在网络上传输数据包并将其路由到目标设备，它为TCP、UDP等传输协议提供了数据传输的基础。IP协议通常被称为网络层协议，而TCP、UDP等协议则属于传输层协议。

```
当您输入一个网址并进入网页时，通常会经过以下协议：

DNS（Domain Name System）协议：您输入的网址首先会被解析成对应的 IP 地址，这个过程需要使用 DNS 协议。

HTTP 或 HTTPS 协议：一旦您的浏览器知道了目标服务器的 IP 地址，它将使用 HTTP 或 HTTPS 协议来建立与该服务器的连接。其中，HTTPS 协议还需要进行 SSL/TLS 握手，以建立加密通道。

TCP（Transmission Control Protocol）协议：一旦建立了连接，浏览器和服务器之间将使用 TCP 协议来传输数据。TCP 协议保证了数据包的传输顺序和完整性，确保了数据传输的可靠性。

HTTP 或 HTTPS 协议：浏览器向服务器发送 HTTP 或 HTTPS 请求，并等待服务器响应。HTTP 请求通常包括请求头、请求体等信息。

服务器处理请求：服务器会根据请求的内容，处理相关逻辑并返回 HTTP 或 HTTPS 响应。HTTP 响应通常包括响应头、响应体等信息。

TCP 协议：服务器向浏览器发送 HTTP 或 HTTPS 响应，也是通过 TCP 协议传输。TCP 协议确保了响应的完整性和顺序。

HTTP 或 HTTPS 协议：浏览器接收到响应后，会解析响应内容并将其呈现在用户界面上。如果响应中包含了其他资源的链接，浏览器会再次发起 HTTP 或 HTTPS 请求来获取这些资源，重复上述过程。
```







