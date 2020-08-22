package main

import "fmt"

type firstS struct {
	in1 int
	in2 int
}
type secondS struct {
	b int
	c float32
	int
	firstS
}

func main() {
	sec := new(secondS)
	sec.b = 6
	sec.c = 7.5
	sec.int = 60
	sec.in1 = 5
	sec.in2 = 10

	fmt.Println(sec)

	sec2 := secondS{6, 7.5, 60, firstS{5, 10}}
	fmt.Println(sec2)
}
