package goroutine

import (
	"fmt"
	"net/http"
	"sync"
	"time"
)

func CalculateQPS() {
	var (
		wg sync.WaitGroup
	)
	f := func() {
		_, _ = http.Get("https://baidu.com")
		wg.Done()
	}

	startTime := time.Now().Unix()
	for i := 0; i < 200; i++ {
		wg.Add(1)
		go f()
	}
	wg.Wait()
	endTime := time.Now().Unix()

	t := endTime - startTime
	fmt.Printf("time: %d\n", t)
	fmt.Printf("qps: %d\n", 16/t)

}
