package goroutine

import (
	"fmt"
	"sync"
)

func PrintNums() {

	var (
		ca = make(chan struct{})
		cb = make(chan struct{})
		wg sync.WaitGroup
		// 交替打印0-4，一共5个数
		limit = 5
	)

	fa := func() {
		for i := 0; i < limit; i += 2 {
			<-ca
			fmt.Println("[fa]", i)
			wg.Done()
			cb <- struct{}{}
		}
	}
	fb := func() {
		for i := 1; i < limit; i += 2 {
			<-cb
			fmt.Println("[fb]", i)
			wg.Done()
			ca <- struct{}{}
		}
	}

	go fa()
	go fb()
	wg.Add(limit)
	ca <- struct{}{}
	wg.Wait()

}
