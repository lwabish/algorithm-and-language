package main

import "fmt"

func main() {
	a := 100
	b := 200
	swap(&a, &b)
	fmt.Println(a)
}

func swap(x *int, y *int) {
	var tmp int
	tmp = *x
	*x = *y
	*y = tmp
}
