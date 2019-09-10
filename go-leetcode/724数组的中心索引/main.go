package main

import "fmt"

func main() {
	fmt.Println(pivotIndex([]int{1, 7, 3, 6, 5, 6}))
	fmt.Println(pivotIndex([]int{1, 2, 3}))
	fmt.Println(pivotIndex2([]int{1, 7, 3, 6, 5, 6}))
	fmt.Println(pivotIndex2([]int{1, 2, 3}))

}

func pivotIndex(nums []int) int {
	var left []int
	var right []int
	for index := range nums {
		left = nums[:index]
		right = nums[index+1:]
		if sum(left) == sum(right) {
			return index
		}
	}
	return -1
}
func pivotIndex2(nums []int) int {
	var leftSum int
	var rightSum int
	rightSum = sum(nums)
	for i, v := range nums {
		if i > 0 {
			leftSum += nums[i-1]
		}
		rightSum -= v
		if leftSum == rightSum {
			return i
		}
		// fmt.Println(leftSum, rightSum)
	}
	return -1
}
func sum(nums []int) int {
	var total int
	for _, v := range nums {
		total += v
	}
	return total
}
