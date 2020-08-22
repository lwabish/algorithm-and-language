package main

import (
	"fmt"
	"strings"
)

type Person struct {
	firstName string
	lastName  string
}

func upPerson(p *Person) {
	p.firstName = strings.ToUpper(p.firstName)
	p.lastName = strings.ToUpper(p.lastName)
}
func main() {
	// 作为值的结构体
	var pers1 Person
	pers1.firstName = "张"
	pers1.lastName = "三三"
	upPerson(&pers1)
	fmt.Println(pers1.firstName, pers1.lastName)

	//作为指针的结构体
	pers2 := new(Person)
	pers2.firstName = "张"
	// 自动给指针指向的变量赋值
	pers2.lastName = "三三"
	// 手动给指针指向的变量赋值
	(*pers2).lastName = "三三"
	upPerson(pers2)
	fmt.Println(pers2.firstName, pers2.lastName)

	//作为字面量的结构体
	pers3 := &Person{"张", "三三"}
	upPerson(pers3)
	fmt.Println(pers3.firstName, pers3.lastName)

}
