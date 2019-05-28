package main

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

	println(employee.ID)
	operateE(employee)
	println(employee.ID)

	println(employee.ID)
	operateE2(&employee)
	println(employee.ID)
}

func operateE(e Employee) {
	e.ID = 222
}
func operateE2(e *Employee) {
	e.ID = 323
}
