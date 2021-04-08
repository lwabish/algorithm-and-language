package main

import "fmt"

type Point struct {
	X, Y int
}
type Circle struct {
	// 匿名成员
	Point
	Radius int
}
type Wheel struct {
	Circle
	Spokes int
}

// 结构体嵌套(继承)
func main() {

	// 字面量中必须写全，不能拍扁用
	w := Wheel{Circle{Point{8, 8}, 4}, 23}

	w1 := Wheel{
		Circle: Circle{
			Point: Point{X: 8, Y: 9},
		},
		Spokes: 20,
	}

	fmt.Printf("%#v\n", w)
	fmt.Printf("%#v\n", w1)

	// 匿名成员在.操作符可以直接省略中间对象-----可以拍扁了用
	w.X = 10
}
