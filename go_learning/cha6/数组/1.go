package main

import (
	"fmt"
)

func main() {
	arr := [5]int{1, 2, 3, 4}
	for i := 0; i < len(arr); i++ {
		fmt.Printf("index:%d,%d\n", i, arr[i])
	}
}
