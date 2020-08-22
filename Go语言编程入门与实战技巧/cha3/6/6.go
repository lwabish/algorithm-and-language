package main

import (
	"fmt"
)

func main() {
	s := "abcd你"
	fmt.Println(s[4:] + "好")
	str := "你好，" +
		"go语言"
	fmt.Println(str)
}
