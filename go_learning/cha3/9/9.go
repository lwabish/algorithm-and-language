package main

import (
	"fmt"
)

func main() {
	s := "hello 世界"
	b := []byte(s)
	b[5] = ','
	fmt.Printf("%s\n", s)
	fmt.Printf("%s\n", b)
}
