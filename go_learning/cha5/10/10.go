package main

import "fmt"

func main() {
	nextNumber := getSequence()
	nextNumber1 := getSequence()

	nextNumber()
	nextNumber()
	nextNumber1()
	nextNumber1()
	nextNumber1()
	fmt.Println(nextNumber(), nextNumber1())
}
func getSequence() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}
