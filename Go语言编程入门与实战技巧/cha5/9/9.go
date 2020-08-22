package main

import (
	"fmt"
)

func main() {
	var f = adder()
	fmt.Println(f(1))
	fmt.Println(f(2))
	fmt.Println(f(4))
}

func adder() func(int) int {
	var x int
	return func(d int) int {
		fmt.Println(x, d)
		x += d
		return x
	}
}
