package main

import (
	"fmt"
	"time"
)

func main() {
	throwsPanic(genErr)
}
func genErr() {
	fmt.Println(time.Now(), "正常语句")
	defer func() {
		fmt.Println(time.Now(), "defer正常")
		panic("第二个错误")
	}()
	panic("第一个错误")
}
func throwsPanic(f func()) (b bool) {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println(time.Now(), "捕获到的异常：", r)
			b = true
		}
	}()
	f()
	return
}
