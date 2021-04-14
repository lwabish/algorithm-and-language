package main

import (
	"fmt"
	"net/url"
)

func main() {
	// Values是一个map的命名类型，因此其既有map本身的方法，同时又包含了新定义的额外方法，比如下面的Add和Get
	m := url.Values{"lang": {"en"}}
	m.Add("item", "1")
	m.Add("item", "2")

	fmt.Println(m.Get("lang"))
	fmt.Println(m.Get("q"))
	// 通过命名map新增的get方法
	fmt.Println(m.Get("item"))
	// 通过map本身的方法
	fmt.Println(m["item"])

	// nil也可以
	m = nil
	// 等价于Value(nil).Get。但是显然不能直接写nil.Get
	fmt.Println(m.Get("item"))
	// 更新nil的map会panic
	// m.Add("item", "3")

}
