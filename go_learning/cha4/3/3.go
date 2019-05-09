package main

import (
	"fmt"
)

func main() {
	i := 1
	// for的三个语句中只有中间不可省略
	for i <= 5 {
		fmt.Println(i)
		i++
	}
	// for range 迭代器
	str := "你好"
	for index, char := range str {
		fmt.Printf("%d:%c\n", index, char)
	}
	// 迭代字典
	m := map[string]int{"a": 1, "b": 2}
	for k, v := range m {
		fmt.Println(k, v)
	}
	// 迭代数组
	numbers := []int{1, 2, 3, 4}
	for i, x := range numbers {
		fmt.Println(i, x)
	}
}
