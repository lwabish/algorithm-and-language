package main

import "fmt"

type Shaper interface {
	Area() float32
}
type Square struct {
	side float32
}
type Rectangle struct {
	length, width float32
}

func (s *Square) Area() float32 {
	return s.side * s.side
}
func (r Rectangle) Area() float32 {
	return r.length * r.width
}
func main() {
	r := Rectangle{5, 3}
	q := &Square{5}
	shapes := []Shaper{Shaper(r), Shaper(q)}
	for n, _ := range shapes {
		fmt.Println(shapes[n], shapes[n].Area())
	}
}
