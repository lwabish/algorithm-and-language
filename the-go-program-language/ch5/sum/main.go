package main

import "fmt"

func main() {
	// 传参调用
	fmt.Println(sum([]int{1, 2, 3}...))
}

// 可变参数，和python类似
// 定义
func sum(vals ...int) int {
	total := 0

	// 使用可变参数
	for _, val := range vals {
		total += val
	}
	return total
}
