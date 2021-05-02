package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("commencing coutdown.")
	tick := time.Tick(1 * time.Second)
	for countdown := 10; countdown > 0; countdown-- {
		fmt.Println(countdown)
		<-tick
	}
	fmt.Println("launched")
}
