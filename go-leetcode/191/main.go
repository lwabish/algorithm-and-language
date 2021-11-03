package main

import (
	"fmt"
	"reflect"
)

func hammingWeight(num uint32) int {
	var count int //存储1的个数
	for num != 0 {
		if num&1 == 1 { //让num与1进行按位与运算，取得num最低位判断是否位1
			count++
		}
		num >>= 1 //num右移一位
	}
	return count
}
func main() {
	var input uint32
	// 为什么input有时候是二进制，有时候是十进制
	// go中0开头的数字是八进制数
	input = 99
	input = 0000000000000000000000110000000
	result := hammingWeight(input)
	fmt.Println(result)
	v := reflect.ValueOf(input)
	fmt.Println(v.Type())
}
