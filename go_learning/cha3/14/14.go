package main

import (
	"fmt"
)

type (
	// 类型别名
	字符串 string
)

var t 字符串 = "abc"

func main() {
	sum := 11
	count := 3
	mean := float32(sum) / float32(count)
	mean2 := sum / count
	fmt.Println(mean)
	fmt.Println(mean2)
	fmt.Println(t)
}
