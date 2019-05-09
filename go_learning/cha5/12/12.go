package main

import (
	"fmt"
)

func main() {
	for i := 0; i < 10; i++ {
		fmt.Println(Fib(i))
	}
}

// Fib ...func Fib(n int)int{}
func Fib(n int) (result int) {
	if n < 2 {
		return n
	}
	return Fib(n-1) + Fib(n-2)
}
