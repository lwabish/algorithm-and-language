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
	var employee Employee

	employee.ID = 1001
	employee.Name = "tom"
	employee.Address = "X"
	employee.Phone = "19999"
	PrintEmployee(&employee)
}
func PrintEmployee(employee *Employee) {
	fmt.Println(employee)
}
