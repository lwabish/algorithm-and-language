package main

import (
	"fmt"
)

func main() {
	s := "abcd你"
	for i := 0; i < len(s); i++ {
		fmt.Println(s[i])
	}

	c := s[len(s)-1]
	fmt.Println(len(s), c)

	fmt.Println(s[0:7])
	fmt.Println(s[:4])
	fmt.Println(s[3:])
}
