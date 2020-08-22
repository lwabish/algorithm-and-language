package main

import (
	"fmt"
)

type S struct {
	Name string
}

func (s S) M1() {
	s.Name = "value"
}
func (s *S) M2() {
	s.Name = "pointer"
}

func main() {
	var s1 = S{"new"}
	var s2 = &s1
	s1.M2()
	fmt.Printf("%+v,%+v\n", s1, s2)
	s1 = S{"new"}
	s2 = &s1
	s2.M1() //指针调用值接收器的方法时，会复制一份值
	fmt.Printf("%+v,%+v\n", s1, s2)
}
