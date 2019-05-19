package main

import "fmt"

func main() {
	// 创建
	slice := make([]int, 100)
	// 等价于
	// slice := []int{99: 0}
	// 同时指定长度和容量
	// slice:=make([]int,2,5)

	for i := range slice {
		slice[i] = i
	}
	// 方括号里的索引是基于底层数组的
	// 长度：从slice[2]-slice[3]
	// 容量：从slice[2]-slice[7]
	newSlice := slice[2:4:8]
	fmt.Println(newSlice)
	fmt.Println(newSlice[1], len(newSlice))

	newSlice2 := slice[3:15]
	newSlice3 := slice[10:15:15]
	// 不写容量，默认是底层后面所有的数组
	println(len(newSlice2), cap(newSlice2))
	// 强行限制容量等于数组，append后即可复制脱离底层
	println(len(newSlice3), cap(newSlice3))

	// 多维切片
	s := [][]int{{10}, {100, 200}}
	s[0] = append(s[0], 2)
	fmt.Println(s)

	// 值传递切片
	s1 := make([]int, 1e6)
	s1 = foo(s1)
}
func foo(slice []int) []int {
	return slice
}
