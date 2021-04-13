package main

import (
	"log"
	"time"
)

func main() {
	bigSlowOperation()
	_ = modifyResult(3)
}
func bigSlowOperation() {
	// 调用时立即执行trace，记录起始时间
	// defer导致返回的函数最后运行
	defer trace("bigSlowOperation")()

	time.Sleep(time.Second * 10)

}

func modifyResult(x int) int {
	result := 2 * x
	// defer加匿名函数，可以读写函数中的变量，比如修改结果
	defer func() { result += 1 }()
	return result
}

func trace(msg string) func() {
	start := time.Now()
	log.Printf("enter %s", msg)
	return func() {
		log.Printf("exit %s (%s)", msg, time.Since(start))
	}
}
