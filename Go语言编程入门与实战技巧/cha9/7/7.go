package main

import (
	"fmt"
	"reflect"
)

func main() {
	var x float64 = 3.4
	v := reflect.ValueOf(x)
	fmt.Println(v.CanSet())
	v = reflect.ValueOf(&x)
	fmt.Println(v.Type())
	fmt.Println(v.CanSet())
	v = v.Elem()
	fmt.Println(v.CanSet())
	v.SetFloat(3.4444)
	fmt.Println(v)
}
