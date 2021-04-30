package main

import (
	"fmt"
)

func main() {
	naturals := make(chan int)
	squares := make(chan int)

	go func() {
		for x := 0; x < 100; x++ {
			naturals <- x
		}
		// 用close关闭channel
		close(naturals)
	}()

	go func() {
		// 用range迭代channel，可以自动实现channel关闭后退出循环
		for x := range naturals {
			squares <- x * x
		}
		close(squares)
	}()

	for x := range squares {
		fmt.Println(x)
	}

}
