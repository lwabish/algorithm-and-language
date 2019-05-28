package main

import (
	"fmt"
)

type Employee struct {
	ID      int
	Name    string
	Address string
	Phone   string
}

func main() {
	var employee1 Employee
	employee1.ID = 10001
	employee1.Name = "TOM"
	employee1.Address = "xxx"
	employee1.Phone = "122333"

	fmt.Println(employee1)
}
