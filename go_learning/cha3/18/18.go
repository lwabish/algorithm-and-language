package main

import (
	"fmt"
)

func main() {
	// 定义一个空指针
	var a *int
	// 又一个指针，指向空指针
	aP := &a

	fmt.Printf("%x\n", a)
	fmt.Printf("%x\n", aP) //&a
	fmt.Printf("%x\n", *aP)
	fmt.Printf("%x\n", &aP)

}
