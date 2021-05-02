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

	// 增加计数器
	var n int
	n++

	go func() { worklist <- os.Args[1:] }()

	seen := make(map[string]bool)

	// 当循环里未能找得到更多链接以增加计数器时，循环最终将终止
	for ; n > 0; n-- {
		list := <-worklist
		for _, link := range list {
			if !seen[link] {
				seen[link] = true
				n++
				go func(link string) {
					worklist <- crawl(link)
				}(link)
			}
		}
	}
}
