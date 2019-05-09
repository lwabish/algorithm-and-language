package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "The quick brown fox jumps over the lazy dog 中文"
	// 由字符串生成slice
	strSli := strings.Fields(str)
	fmt.Println(strSli)
	// 迭代slice
	for _, val := range strSli {
		fmt.Println(val)
	}
	// 将slice黏合
	fmt.Println(strings.Join(strSli, ";"))
}
