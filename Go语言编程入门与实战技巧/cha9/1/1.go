package main

type Shaper interface {
	Area() float32
	// Abc() float32
}

type Square struct {
	side float32
}

func (sq *Square) Area() float32 {
	return sq.side * sq.side
}

// 结构体square+square的方法area，实现了接口shaper
func main() {
	sq1 := new(Square)
	sq1.side = 5

	// areaIntf=sq1
	areaIntf := Shaper(sq1)
	// areaIntf := sq1
	println(areaIntf.Area())
}
