package main

import (
	"fmt"
	"reflect"
)

func main() {
	var x float64 = 3.1415
	v := reflect.ValueOf(x)
	// v.SetFloat(3.1415)
	fmt.Println("v:", v.CanSet())
	v = reflect.ValueOf(&x)
	fmt.Println("v的类型", v.Type())
	fmt.Println("v:", v.CanSet())
	v = v.Elem()
	fmt.Println("v的Elem是：", v)
	fmt.Println("v:", v.CanSet())
	v.SetFloat(3.14155)
	fmt.Println(v.Interface())
	fmt.Println(v)
}
