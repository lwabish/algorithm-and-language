package main

import "fmt"

func main() {
	fmt.Println(Factorial(15))
}

func Factorial(n uint64) (result uint64) {
	if n == 0 {
		return 1
	}
	return n * Factorial(n-1)
}
