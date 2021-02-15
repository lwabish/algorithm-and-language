package tempconv

import "fmt"

// Celsius(xxx) 类型转换，不是函数调用
type Celsius float64

/*
对于每一个类型T，都有一个对应的类型转换操作T(x)，用于将x转为T类型
（译注：如果T是指针类型，可能会需要用小括弧包装T，比如(*int)(0)）
*/
type Fahrenheit float64

const (
	AbsoluteZeroC Celsius = -273.15
	FreezingC     Celsius = 0
	BoilingC      Celsius = 100
)

func (c Celsius) string() string {
	return fmt.Sprintf("%gC", c)
}
func (f Fahrenheit) string() string {
	return fmt.Sprintf("%gF", f)
}

