package main

import (
	"fmt"
	"reflect"
)

type NotknownType struct {
	s1, s2, s3 string
}

func (n NotknownType) String() string {
	return n.s1 + "-" + n.s2 + "-" + n.s3
}

var secret interface{} = NotknownType{"google", "go", "code"}

func main() {
	value := reflect.ValueOf(secret)
	typ := reflect.TypeOf(secret)
	fmt.Println(typ)
	knd := value.Kind()
	fmt.Println(knd)

	// 迭代结构的字段
	for i := 0; i < value.NumField(); i++ {
		fmt.Printf("field %d: %v\n", i, value.Field(i))
		// value.Field(i).SetString("dd")
		// 只有大写的被导出字段可以修改
	}
	results := value.Method(0).Call(nil)
	fmt.Println(results)
}
