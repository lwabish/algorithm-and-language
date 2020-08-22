package main

import (
	"fmt"
)

func main() {
	test()
}
func test() {
	defer func() {
		fmt.Println(recover())
		// 有效，defer中的匿名函数
	}()
	defer func() {
		func() {
			recover()
			// 间接调用，无效
		}()
	}()

	defer fmt.Println(recover()) //直接调用，无效
	defer recover()
	// 无效，直接调用
	panic("发生错误")
}
