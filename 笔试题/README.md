# 笔试题
<!-- TOC -->
* [笔试题](#笔试题)
  * [slice](#slice)
  * [byte](#byte)
  * [recover](#recover)
  * [interface](#interface)
  * [string](#string)
    * [1](#1)
    * [2](#2)
  * [map](#map)
  * [struct](#struct)
  * [channel](#channel)
<!-- TOC -->
## slice

```go
package main

import "fmt"

func TestSlice(arr []int) {
	arr = append(arr, 3)
	arr = append(arr, 4)
}

func main() {
	arr := make([]int, 1, 10)
	arr = append(arr, 1)
	arr = append(arr, 2)
	TestSlice(arr)
	fmt.Printf("%d,%d,%d", arr[0], arr[1], len(arr))
}

```

这个 Go 程序使用函数创建了一个长度为 1、容量为 10 的整数切片make。然后它将值 1 和 2 附加到切片并将切片传递给函数TestSlice。

在函数内部TestSlice，切片附加值 3 和 4。但是，由于切片在 Go 中是通过引用传递的，因此当切片传递给函数时不会创建新切片。相反，该函数对作为参数传递的原始切片进行操作。

在这种情况下，由于TestSlice函数不返回任何值，因此修改后的切片不会传回给函数main。因此，当程序打印 中切片的值时main，它会打印原始值附加
1 和 2：（0,1,3假设arr[0]为 0）。

因此，该程序的输出将是0,1,3.

## byte

```go
package main

import (
	"fmt"
)

var item = "hello"

func main() {
	v := item
	v[0] = 'a'
	fmt.Printf("%s", item)
}

```
由于类型错误，您提供的代码将无法编译。这是因为v，它是一个类型的变量string，正在被赋值为item，这也是一个字符串。在 Go 中，字符串是不可变的，这意味着字符串一旦创建，其内容就无法更改。

因此，当代码尝试v通过将 的值赋给来修改第一个字符'a'时，将发生类型错误，因为无法以这种方式修改字符串。

要修复此错误，可以使用字节切片而不是字符串，因为字节切片是可变的。
## recover

```go
package main

import "fmt"

func main() {
	Defer("John")
}

func Defer(name string) {
	defer func(param string) {
		fmt.Printf("%s", param)
	}(name)

	defer func() {
		err := recover()
		if err != nil {
			fmt.Printf("%s", err)
		}
	}()
	name = "Lee"
	panic("error")
	defer func() {
		fmt.Printf("end")
	}()
}
```

给定的 Go 代码定义了一个Defer接受字符串参数的函数name。该main函数使用Defer参数“John”调用函数。

该Defer函数具有三个延迟函数。第一个延迟函数有一个闭包，param它接受一个字符串参数并使用fmt.Printf().
的值是传递给函数的参数param的值。nameDefer

fmt.Printf()如果发生恐慌，第二个延迟函数会从恐慌中恢复，并在出现错误时使用打印错误消息。将变量的值修改为“Lee”panic()
后调用该函数。name

第三个延迟函数使用fmt.Printf().

当panic()调用该函数时，它会导致运行时错误并立即终止程序执行。但是，在终止程序执行之前，它会按照将延迟函数添加到延迟堆栈的相反顺序执行延迟函数。
因此，该程序的输出将是：
`errorJohn`

将变量的值修改为“Lee”panic()
后调用该函数。name然而，第一个延迟函数打印参数的值param，这是“John”，因为它被传递给了函数Defer。因此，第一个输出是“John”。第二个延迟函数从恐慌中恢复并打印错误消息，即“error”。最后，第三个延迟函数打印“end”。但是，第三个延迟函数永远不会执行，因为程序在
panic 之后终止。

## interface

```go

package main

import (
	"fmt"
)

func main() {
	var object interface{}
	object = 1
	switch object.(type) {
	case int:
		switch object {
		case 1:
			fmt.Printf("1")
		case 2:
			fmt.Printf("2")
		case 3:
			fmt.Printf("3")
			break
		case 4:
			fmt.Printf("4")
			break
		default:
			fmt.Printf("Unknown int value: %v", object)
		}
	default:
		fmt.Printf("Unknown type: %T", object)
	}

}

```

此代码检查 的基础类型是否object为int，如果是，则执行内部 switch 语句以确定打印哪种情况。如果object不是int，它会向控制台打印一条消息，指示未知类型。

## string
### 1
```go

package main

import (
	"fmt"
)

func main() {
	name := "张三"
	fmt.Printf("%d", len(name))
}

```

函数len返回字符串中的字节数，这与字符数不同，因为有些字符可能占用多个字节。

在这个程序中，变量name被赋值为字符串“张三”。该fmt.Printf函数用于打印name使用%d格式说明符的长度，该格式说明符用于打印整数值。

该程序运行时，会输出字符串“张三”的字节数。实际输出将取决于系统的编码及其表示汉字的方式，但它可能是 6 个或 9
个字节，因为字符“张”和“三”在 UTF-8 编码中可以分别由三个字节表示。
### 2
在 Go 中，字符串是不可变的，这意味着一旦创建了一个字符串，就不能直接修改它。因此，如果想要修改字符串，我们必须先将其转换为可变的类型，例如切片或字节数组，然后再修改它。

使用字节数组比使用字符串切片更高效，因为字节数组可以直接修改，而不需要分配新的内存空间。以下是使用字节数组来将 "hello" 修改为 "h周llo" 的示例代码：
```go
package main

import "fmt"

func main() {
	str := "hello"
	bytes := []byte(str)         // 将字符串转换为字节数组
	bytes[1] = '周'              // 修改字节数组中的第二个字符
	modifiedStr := string(bytes) // 将字节数组转换为字符串
	fmt.Println(modifiedStr)     // 输出：h周llo
}

```
## map

```go
package main

import "fmt"

func main() {
	var peoples map[string]string = make(map[string]string)
	peoples["001"] = "Jack"
	peoples["004"] = "John"
	peoples["003"] = "Georgia"
	peoples["002"] = "Lucy"
	for k, v := range peoples {
		fmt.Println(k, v)
	}
}

```

请注意，每次运行程序时键值对的顺序可能不同，因为映射不保留其元素的顺序。

## struct

```go
package main

import (
	"fmt"
)

type People struct {
	age  *int
	name string
}

func (p People) SetAge(age int) {
	p.age = &age
}

func (p People) GetAge() int {
	return *p.age
}

func (p People) SetName(name string) {
	p.name = name
}

func (p People) GetName() string {
	return p.name
}
func NewPeople(name string, age int) (p *People) {
	p = new(People)
	p.age = new(int)
	p.SetName(name)
	p.SetAge(age)
	return
}

func main() {
	var people *People = NewPeople("John", 22)
	people.SetName("Grace")
	people.SetAge(45)
	fmt.Printf("%s,%d", people.GetName(), people.GetAge())
}

```
## channel
```go

```