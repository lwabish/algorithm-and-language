package main

import (
	"fmt"
	"log"
	"os"

	"gopl.io/ch5/links"
)

var tokens = make(chan struct{}, 20)

func crawl(url string) []string {
	fmt.Println(url)
	// 向channel写，如果没超过20，写入成功，获取了锁，可以继续，否则阻塞等待
	tokens <- struct{}{}
	list, err := links.Extract(url)
	<-tokens
	if err != nil {
		log.Print(err)
	}
	return list
}

func main() {
	worklist := make(chan []string)

	// 因为无缓存的channel必须放进去立马有人消费，所以这里需要放到另外的goruntine，避免阻塞下面对channel的迭代
	go func() {
		worklist <- os.Args[1:]
	}()

	seen := make(map[string]bool)
	for list := range worklist {
		for _, link := range list {
			if !seen[link] {
				seen[link] = true
				go func(link string) {
					worklist <- crawl(link)
				}(link)
			}
		}
	}
}
