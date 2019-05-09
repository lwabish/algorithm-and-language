package main

import "fmt"

func main() {
	age := ageMinOrMax("min", 1, 2, 3, 4)
	fmt.Println(age)

	ageArr := []int{1, 2, 3, 4, 5}
	age = ageMinOrMax("max", ageArr...)
	fmt.Println(age)
}
func ageMinOrMax(m string, a ...int) int {
	if len(a) == 0 {
		return 0
	}
	if m == "max" {
		max := a[0]
		for _, v := range a {
			if v > max {
				max = v
			}
		}
		return max
	} else if m == "min" {
		min := a[0]
		for _, v := range a {
			if v < min {
				min = v
			}
		}
		return min
	} else {
		return -1
	}
}
