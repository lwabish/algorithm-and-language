package main

import (
	"fmt"
	"github.com/lwabish/algorithm-and-language/go-book-Huang/cha8/16/person"
)

func main() {
	p := new(person.Person)
	p.SetFirstName("wubowen")
	fmt.Println(p.FirstName())
}
