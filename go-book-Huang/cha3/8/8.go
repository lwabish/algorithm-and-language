package main

import (
	"fmt"
)

func main() {
	s := "我是中国人"
	for i := 0; i < len(s); i++ {
		fmt.Printf("%c", s[i])
	}
	fmt.Println("")
	for _, v := range s {
		fmt.Printf("%c", v)
	}
}
