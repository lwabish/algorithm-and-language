package main

import (
	"fmt"
	"os"
	"time"
)

func main() {
	abort := make(chan struct{})

	go func() {
		os.Stdin.Read(make([]byte, 1))
		abort <- struct{}{}
	}()

	fmt.Println("commencing coutdown.press return to abort")

	select {
	case <-time.After(10 * time.Second):
	case <-abort:
		fmt.Println("aborted")
		return
	}
	fmt.Println("launched")

}
