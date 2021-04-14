package main

import "image/color"

type Point struct {
	X, Y float64
}

type ColoredPoint struct {
	// 可以获得它的属性和方法
	// 但是不完全和继承一样，在方法参数中，父子不能混用
	Point
	Color color.RGBA
}
