package main

import (
	"fmt"
	"log"
	"math/rand"
	"os"
	"sync"
	"time"
)

func main() {
	makeT5([]string{"1", "2", "3", "4"})
}

// 模拟一个耗时操作
func ImageFile(infile string) (string, error) {
	time.Sleep(time.Duration(rand.Intn(5) * int(time.Second)))
	return infile, nil
}

// 顺序执行
func makeT(filenames []string) {
	for _, f := range filenames {
		if _, err := ImageFile(f); err != nil {
			log.Println(err)
		}
	}
}

// 将顺序执行改为多个goroutine并行
func makeT2(filenames []string) {
	for _, f := range filenames {
		go ImageFile(f)
	}
}

// goruntine执行完后给主线程通知，主线程等所有完成后再退出
func makeT3(filenames []string) {
	ch := make(chan string)

	for _, f := range filenames {
		// 不直接在goruntine中引用f（闭包），每次启动goroutine时动态地传参，确保准确地将当前f传给goroutine
		go func(f string) {
			ImageFile(f)
			// 完成后向channel发
			fmt.Println(f, "send done")
			ch <- f
		}(f)
	}

	// 因为这里迭代的是filenames slice，所以是有限次迭代
	for _, v := range filenames {
		fmt.Println("waiting: ", v)
		// 此处会阻塞，一定会按照迭代顺序等待所有都完成
		fmt.Println("received: ", <-ch)
	}
}

// 有bug：有err从goroutine返回后，channel未被排空，其他goroutine向channel中发送会被阻塞住：goruntine泄露
func makeT4(filenames []string) error {
	errors := make(chan error)

	for _, f := range filenames {
		go func(f string) {
			_, err := ImageFile(f)
			errors <- err
		}(f)
	}

	for range filenames {
		if err := <-errors; err != nil {
			return err
		}
	}
	return nil
}

func makeT5(filenames []string) (thumbfiles []string, err error) {
	type item struct {
		thumbfile string
		err       error
	}

	ch := make(chan item, len(filenames))

	for _, f := range filenames {
		go func(f string) {
			var it item
			it.thumbfile, it.err = ImageFile(f)
			ch <- it
		}(f)
	}

	for range filenames {
		it := <-ch
		if it.err != nil {
			return nil, it.err
		}
		thumbfiles = append(thumbfiles, it.thumbfile)
	}
	return thumbfiles, nil
}

func makeT6(filenames <-chan string) int64 {
	sizes := make(chan int64)
	var wg sync.WaitGroup
	for f := range filenames {
		// 计数一定要在主线程中，必须比wg.Wait()早
		wg.Add(1)

		go func(f string) {
			// 即使出错也要减一
			defer wg.Done()
			thumb, err := ImageFile(f)
			if err != nil {
				log.Println(err)
				return
			}
			info, _ := os.Stat(thumb)
			sizes <- info.Size()
		}(f)
	}

	// 一个独立的goroutine，监视着wg是否为0，最后把channel关闭
	go func() {
		wg.Wait()
		close(sizes)
	}()

	var total int64
	// 迭代channel，channel关闭后自动退出循环
	for size := range sizes {
		total += size
	}
	return total
}
