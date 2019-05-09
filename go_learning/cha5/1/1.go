package main

import "fmt"

func main() {
	x := 1
	y := 2
	z := 3
	maxNum := max(x, y)
	fmt.Println(maxNum)
	maxNum = max(x, z)
}

func max(a, b int) (maxNum int) {
	if a > b {
		return a
	}
	return b
}
func Max(a, b int) (maxNum int) {
	if a > b {
		maxNum = a
	} else {
		maxNum = b
	}
	return
}
