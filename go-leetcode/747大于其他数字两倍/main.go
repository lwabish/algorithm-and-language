package main

import "fmt"

func main() {
	fmt.Println(dominantIndex([]int{3, 6, 1, 0}))
	fmt.Println(dominantIndex([]int{1, 2, 3, 4}))
	fmt.Println(dominantIndex([]int{0, 0, 3, 2}))

}

func dominantIndex(nums []int) int {
	var first int
	var second int
	var firstIndex int
	for i, v := range nums {
		if v > first {
			first, second = v, first
			firstIndex = i
		} else if v > second {
			second = v
		}
	}
	if first >= 2*second {
		return firstIndex
	}
	return -1
}
