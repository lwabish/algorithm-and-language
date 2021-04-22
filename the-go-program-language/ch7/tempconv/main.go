package main

import (
	"flag"
	"fmt"
)

type Celsius float64

type Fahrenheit float64

func FToC(f Fahrenheit) Celsius { return Celsius((f - 32) * 5 / 9) }

type celsiusFlag struct{ Celsius }

// 实现String
// TODO: 为什么换成celsiusFlag的方法后，输出会只有数字
func (c Celsius) String() string {
	fmt.Println("abc")
	return fmt.Sprintf("%gC", c)
}
func (c *celsiusFlag) String() string {
	fmt.Println("sdfsdf")
	return "2222"
}

// 实现Set方法
func (f *celsiusFlag) Set(s string) error {
	var unit string
	var value float64
	fmt.Sscanf(s, "%f%s", &value, &unit)
	switch unit {
	case "C", "°C":
		f.Celsius = Celsius(value)
		return nil
	case "F", "°F":
		f.Celsius = FToC(Fahrenheit(value))
		return nil
	}
	return fmt.Errorf("invalid temp %q", s)
}

func CelciusFlag(name string, value Celsius, usage string) *Celsius {
	f := celsiusFlag{value}
	// 将实现了flag.Value接口的实例传给Var方法
	flag.CommandLine.Var(&f, name, usage)
	return &f.Celsius
}

// 使用自定义的arg
func main() {
	// var temp = CelciusFlag("temp", 20.0, "the temperature")
	// flag.Parse()
	// fmt.Println(*temp)
	c := celsiusFlag{12.0}
	fmt.Println(c)
}
