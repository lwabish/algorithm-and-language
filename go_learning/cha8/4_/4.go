package main

import (
	"fmt"

	"./struct_pack/structpack"
)

func main() {
	s1 := new(structpack.ExpStruct)
	s1.Mi1 = 10
	s1.Mf1 = 16.
	fmt.Println(s1)
}
