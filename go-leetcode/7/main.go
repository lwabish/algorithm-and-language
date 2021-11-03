package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(reverse(1234567))
	fmt.Println(reverse(12345678999999999))

}

// reverse: 整数反转，不允许出现溢出的32位整数
func reverse(x int) int {
	var res int
	for x != 0 {
		// 直接判断，可能已经溢出。需要提前利用一个结论把判断条件转化https://leetcode-cn.com/problems/reverse-integer/solution/zheng-shu-fan-zhuan-by-leetcode-solution-bccn/
		if res > math.MaxInt32/10 || res < math.MinInt32/10 {
			return 0
		}
		digit := x % 10
		x /= 10
		res = res*10 + digit
	}
	return res
}
