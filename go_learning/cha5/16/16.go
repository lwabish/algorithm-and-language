package main

import (
	"fmt"
	"time"
)

func main() {
	i, p := a()
	fmt.Println(i, p, time.Now())

}

func a() (i int, p *int) {
	// i++
	// func定义时i初始化为0
	defer func(i int) {
		fmt.Println("defer3:", i, &i, time.Now())
	}(i)

	// i是return里的i，初始化也是0
	defer fmt.Println("defer2:", i, &i, time.Now())

	//
	defer func() {
		fmt.Println("defer1:", i, &i, time.Now())
	}()

	i++

	// 匿名函数，闭包继承了外面的i
	func() {
		fmt.Println("print1:", i, &i, time.Now())
	}()

	// 当前作用域的i
	fmt.Println("print2:", i, &i, time.Now())
	return i, &i
}
