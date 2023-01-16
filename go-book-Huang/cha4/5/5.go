package main

import (
	"fmt"
)

func main() {
	defer fmt.Println("finished")
	fmt.Println("started")
	reversePrint()
}
func print(i int) {
	fmt.Println(i)
}
func reversePrint() {
	for i := 0; i < 5; i++ {
		defer print(i)
	}
}
