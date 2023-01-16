package main

import (
	"fmt"
)

func main() {
	value1 := 1.0
	value2 := 1.0000000000000001
	if value1 == value2 {
		fmt.Println("equal")
		//float64精度在15位，后面的被舍弃，所以比较结果是相等
	}
}
