package main

import (
	"fmt"
)

var value1 float64

func main() {
	s := "aA 你2"
	fmt.Println("字符串长度：", len(s))
	for i := 0; i < len(s); i++ {
		fmt.Println(s[i])
	}
	// s := "aaaa"
	// 字符串不能直接修改
	t := s
	s += "世界"
	o := `
	dsf
	sdfs
	`
	fmt.Println(t)
	fmt.Println(s)
	fmt.Println("\a")
	fmt.Println(o)
}
