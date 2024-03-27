package goroutine

import (
	"fmt"
	"sync"
)

func PrintAsChain() {
	var (
		ca = make(chan struct{})
		cb = make(chan struct{})
		cc = make(chan struct{})
		wg sync.WaitGroup
	)

	fa := func() {
		<-ca
		fmt.Println("a")
		wg.Done()
		cb <- struct{}{}
	}

	fb := func() {
		<-cb
		fmt.Println("b")
		wg.Done()
		cc <- struct{}{}
	}

	fc := func() {
		<-cc
		fmt.Println("c")
		wg.Done()
		ca <- struct{}{}
	}
	go fa()
	go fb()
	go fc()
	wg.Add(3)
	ca <- struct{}{}
	wg.Wait()

}
