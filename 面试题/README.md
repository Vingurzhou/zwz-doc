

## 面试题

  - [go](#go)
    - [gmp](#gmp)
    - [channel状态](#channel状态)
    - [结构体比较](#结构体比较)
    - [make和new区别](#make和new区别)
    - [时间函数增加一天](#时间函数增加一天)
    - [goroutine内跑goroutine什么时候结束](#goroutine内跑goroutine什么时候结束)
  - [redis](#redis)
    - [持久化](#持久化)
      - [RDB](#rdb)
      - [AOF](#aof)
    - [集群](#集群)
    - [哨兵](#哨兵)
## go

### gmp

* G（Goroutine）：即Go协程，每个go关键字都会创建一个协程。
* M（Machine）：工作线程，在Go中称为Machine，数量对应真实的CPU数（真正干活的对象）。
* P（Processor）：处理器（Go中定义的一个摡念，非CPU），包含运行Go代码的必要资源，用来调度 G 和 M 之间的关联关系，其数量可通过
  GOMAXPROCS() 来设置，默认为核心数。

M必须拥有P才可以执行G中的代码，P含有一个包含多个G的队列，P可以调度G交由M执行。

### channel状态

Channel是异步进行的, channel存在3种状态：

* nil，未初始化的状态，只进行了声明，或者手动赋值为nil
* active，正常的channel，可读或者可写
* closed，已关闭，千万不要误认为关闭channel后，channel的值是nil

| 操作   | 一个零值nil通道 | 一个非零值但已关闭的通道 | 一个非零值且尚未关闭的通道 |
|------|-----------|--------------|---------------|
| 关闭   | 	产生恐慌     | 	产生恐慌        | 	成功关闭         |
| 发送数据 | 	永久阻塞     | 	产生恐慌        | 	阻塞或者成功发送     |
| 接收数据 | 	永久阻塞     | 	永不阻塞        | 	阻塞或者成功接收     |

### 结构体比较

### make和new区别

用new还是make？到底该如何选择？

* make 仅用来分配及初始化类型为 slice、map、chan 的数据。
* new 可分配任意类型的数据，根据传入的类型申请一块内存，返回指向这块内存的指针，即类型 *Type。
* make 返回引用，即 Type，new 分配的空间被清零， make 分配空间后，会进行初始。

### 时间函数增加一天

`time.Now().AddDate(0, 0, 1)
`

### goroutine内跑goroutine什么时候结束

## redis

### 持久化

#### RDB

#### AOF

### 集群

### 哨兵




