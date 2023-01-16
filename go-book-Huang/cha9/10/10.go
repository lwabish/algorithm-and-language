package main

import (
	"os"
	"strconv"
)

type Stringer interface {
	String() string
}
type Celsius float64

func (c Celsius) String() string {
	return strconv.FormatFloat(float64(c), 'f', 1, 64) + "@C"
}

type Day int

var dayName = []string{
	"yi",
	"er",
	"san",
	"si",
	"wu",
	"liu",
	"qi",
}

func (d Day) String() string {
	return dayName[d]
}
func print(args ...interface{}) {
	for i, arg := range args {
		if i > 0 {
			os.Stdout.WriteString(" ")
		}
		switch a := arg.(type) {
		case Stringer:
			os.Stdout.WriteString(a.String())
		case int:
			os.Stdout.WriteString(strconv.Itoa(a))
		case string:
			os.Stdout.WriteString(a)
		default:
			os.Stdout.WriteString("???")
		}
	}
}
func main() {
	print(Day(1), Celsius(18.36))
}
