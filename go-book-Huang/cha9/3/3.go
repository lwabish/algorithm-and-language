package main

import "fmt"

type stockPosition struct {
	ticker     string
	sharePrice float32
	count      float32
}

func (s stockPosition) getValue() float32 {
	return s.sharePrice * s.count
}

type car struct {
	make  string
	model string
	price float32
}

func (c car) getValue() float32 {
	return c.price
}

type valuable interface {
	getValue() float32
}

//	func showValue(asset valuable) {
//		fmt.Println(asset.getValue())
//	}
func main() {
	o := stockPosition{"goog", 567.1, 4}
	fmt.Println(valuable(o).getValue())
	fmt.Println(valuable(car{"a", "b", 4444}).getValue())
}
