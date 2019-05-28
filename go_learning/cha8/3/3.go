package main

import "fmt"

type number struct {
	f float32
}
type nr number //类型别名
func main() {
	a := number{5.0}
	b := nr{5.0}
	// float(b)|c=b|不合法
	var c = number(b)
	fmt.Println(a, b, c)

}
