package main

import (
	"fmt"
)

//Pi:
const Pi = 3.1415926
const Pi2 float32 = 3.1415

// const LongPi=3.1444444444444.
// 			33333333333333333415.
// 11111111111111111111111111111111926
const Return = true
const Hello = "你好"
const s = "我"
const l = len(Hello)
const l2 = len(s)
const (
	Monday, Tuesday = 1, 2
)
const (
	a = iota
	b
	c
	d, e, f = iota, iota, iota
	g       = iota
	h       = "h"
	i
	j = iota
)
const z = iota

var aa, bb, cc = 1, 2, 3
var a1, a2 int
var a3, a4 int = 1, 2

func main() {
	fmt.Println(a, b, c, d, e, f, g, h, i, j, z)
}
