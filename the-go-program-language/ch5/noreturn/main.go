package main

import "fmt"

func main() {
	a := noReturnButReturn()
	fmt.Println(a)
}

// 没有return但是可以return值
// panic后recover可以拿到panic的值，并且修改返回值
func noReturnButReturn() (result int) {
	defer func() {
		if p := recover(); p != nil {
			result = p.(int)
		}
	}()
	panic(3)
}
