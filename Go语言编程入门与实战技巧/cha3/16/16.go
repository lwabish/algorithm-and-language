package main

import (
	"fmt"
)

func main() {
	a := 20
	ap := &a
	fmt.Println(&a)
	fmt.Println(ap)
	fmt.Println(*ap)
}
