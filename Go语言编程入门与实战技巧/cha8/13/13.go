package main

import (
	"time"
)

type myTime struct {
	// 非本地定义的包，定义成别名类型，即可有方法
	time.Time
}

func main() {
	m := myTime{time.Now()}
	println(m.first3Chars())
}
func (self myTime) first3Chars() string {
	return self.Time.String()[0:3]
}
