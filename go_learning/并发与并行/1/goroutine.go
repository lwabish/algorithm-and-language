package main

import (
	"time"
)

func printNumbers1() {
	for i := 0; i < 10; i++ {
		// fmt.Printf("%d ", i)
	}
}
func printLetters1() {
	for i := 'A'; i < 'A'+10; i++ {
		// fmt.Printf("%c ", i)
	}
}
func print1() {
	printNumbers1()
	printLetters1()
}
func goPrint1() {
	go printLetters1()
	go printNumbers1()
}
func main() {}

func printLetters2() {
	time.Sleep(1 * time.Microsecond)
	for i := 'A'; i < 'A'+100; i++ {
		// fmt.Printf("%c ", i)
	}
}
func printNumbers2() {
	time.Sleep(1 * time.Microsecond)
	for i := 1; i < 100; i++ {
		// fmt.Printf("%d ", i)
	}
}
func print2() {
	printNumbers2()
	printLetters2()
}
func goPrint2() {
	go printLetters2()
	go printNumbers2()
}
