package main

import (
	"fmt"
	"reflect"
)

type T struct {
	A int
	B string
}

func main() {
	t := T{23, "hello"}

	// 指针+elem即可得到原对象
	s := reflect.ValueOf(&t).Elem()

	typeOfT := s.Type()
	for i := 0; i < s.NumField(); i++ {
		f := s.Field(i)
		fmt.Printf("%d:%s %s = %v\n", i, typeOfT.Field(i).Name, f.Type(), f.Interface())
	}

	s.Field(0).SetInt(77)
	s.Field(1).SetString("sss")
	fmt.Println(t)
}
