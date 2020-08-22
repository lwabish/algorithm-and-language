package main

import (
	"fmt"
)

func main() {
	s := "hello 世界"
	r := []rune(s)
	r[6] = '中'
	r[7] = '国'
	fmt.Printf(string(r))
}
