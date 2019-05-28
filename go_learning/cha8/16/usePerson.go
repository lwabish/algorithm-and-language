package main

import (
	"fmt"

	"./person"
)

func main() {
	p := new(person.Person)
	p.SetFirstName("wubowen")
	fmt.Println(p.FirstName())
}
