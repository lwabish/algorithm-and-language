package main

import (
	"fmt"
)

var x interface{} //空接口
func main() {
	marks := 55
	//目标对象在case里
	switch {
	case marks > 89:
		fmt.Println("1")
	case marks > 79:
		fmt.Println("2")
	default:
		fmt.Println("a")
	}
	//目标对象在case外
	switch marks {
	case 55:
		fmt.Println("good")
	}
	//针对接口的类型switch
	x = 1
	switch i := x.(type) {
	case nil:
		fmt.Println(i)
	case int:
		fmt.Println(i)
	}
	//switch初始化
	switch marks := 90; marks {
	case 90:
		fmt.Println("90")
	}

}
