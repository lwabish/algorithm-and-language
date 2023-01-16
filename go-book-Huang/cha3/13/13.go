package main

import (
	"fmt"
	"strconv"
)

func main() {
	orig := "233"
	fmt.Printf("%T,%d\n", orig, strconv.IntSize)

	num, err := strconv.Atoi(orig)
	fmt.Printf("%T,%d\n", num, num)
	fmt.Println(err)
	num += 5
	newS := strconv.Itoa(num)
	fmt.Println(newS)
}
