package main

import (
	"fmt"
	"math"
)

type Square struct {
	side float32
}
type Circle struct {
	radius float32
}
type Shaper interface {
	Area() float32
}

func (sq *Square) Area() float32 {
	return sq.side * sq.side
}
func (c *Circle) Area() float32 {
	return math.Pi * c.radius * c.radius
}
func main() {
	var areaI Shaper
	sq1 := new(Square)
	sq1.side = 5

	areaI = sq1
	if t, ok := areaI.(*Square); ok {
		println(t)
	}
	if u, ok := areaI.(*Circle); ok {
		fmt.Println(u)
	} else {
		fmt.Println("areaI不含类型为Circle的变量")
	}
}
