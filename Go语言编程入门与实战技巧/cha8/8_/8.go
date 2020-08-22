package main

import (
	"fmt"
	"reflect"
)

type TagType struct {
	field1 bool
	field2 string
	field3 int
}

func main() {
	tt := TagType{true, "iphone x", 1}
	for i := 0; i < 3; i++ {
		refTag(tt, i)
	}
}
func refTag(tt TagType, ix int) {
	ttType := reflect.TypeOf(tt)
	ixField := ttType.Field(ix)
	fmt.Printf("%v", ixField.Tag)
}
