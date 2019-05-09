package main

import (
	"fmt"
)

func main() {
	b()
}
func a() {
	defer un(trace("a"))
	fmt.Println("a的逻辑")
}
func b() {
	defer un(trace("b"))
	fmt.Println("b的逻辑")
	a()
}
func trace(s string) string {
	fmt.Println("开始执行", s)
	return s
}

func un(s string) {
	fmt.Println("结束执行", s)
}
