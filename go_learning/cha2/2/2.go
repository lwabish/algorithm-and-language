package main

import "fmt"

var a = 1

// a:=10 wrong
func main() {
	b := 2
	a = 100
	fmt.Println(a)

	a := "hello"
	fmt.Println(a, b, c)

}

var c = 0
