package main

import "math"

type Point struct {
	X, Y float64
}

// Distance 是普通函数
func Distance(p, q Point) float64 {
	return math.Hypot(q.X-p.X, q.Y-p.Y)
}

// Distance 是Point的方法
func ( /*方法的接收器*/ p Point) Distance(q Point) float64 {
	return math.Hypot(q.X-p.X, q.Y-p.Y)
}
