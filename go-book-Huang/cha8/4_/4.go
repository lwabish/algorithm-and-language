package main

import (
	"fmt"
	structpack "github.com/lwabish/algorithm-and-language/go-book-Huang/cha8/4_/struct_pack"
)

func main() {
	s1 := new(structpack.ExpStruct)
	s1.Mi1 = 10
	s1.Mf1 = 16.
	fmt.Println(s1)
}
