package main

import "fmt"

type myStruct struct {
	i1  int
	f1  float32
	str string
}

func main() {
	ms := new(myStruct)
	ms.i1 = 10
	ms.f1 = 15.5
	ms.str = "google"
	println(ms.i1)
	fmt.Println(ms.f1)
	println(ms.str)
	fmt.Println(ms)
}
