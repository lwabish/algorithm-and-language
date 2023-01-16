package main

import (
	"fmt"
)

func main() {
	// 空指针
	var ptr *int
	// fmt.Printf("%x\n", *ptr)因为是空指针，所以不能引用
	fmt.Printf("%x\n", ptr)
	fmt.Printf("%x\n", &ptr)

	data := 1
	// 非空指针
	var ptr1 = &data
	fmt.Printf("%x\n", *ptr1)
	fmt.Printf("%x,", ptr1)
	fmt.Printf("%x\n", &data)
	fmt.Printf("%x\n", &ptr1)

	if ptr == nil {
		println("empty")
	}
	// *ptr = 10
	// 对空指针使用会使程序崩溃
}
