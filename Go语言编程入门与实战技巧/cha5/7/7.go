package main

import "fmt"

func main() {
	fmt.Println(Add()(3))
	fmt.Println(Add2(3)(3))
}
func Add() func(b int) int {
	return func(b int) int {
		return b + 2
	}
}

func Add2(a int) func(b int) int {
	return func(b int) int {
		return a + b
	}
}
