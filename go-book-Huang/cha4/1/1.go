package main

import (
	"fmt"
)

func main() {
	if a := 10; a > 20 {
		fmt.Println("top")
	} else if a > 10 {
		fmt.Println("med")
	} else {
		fmt.Println("bottom")
	}
}
