package main

import (
	"fmt"
)

func main() {
	s := "你"
	t := "好"
	if t > s {
		for i := 0; i < 3; i++ {
			fmt.Println(s[i], t[i])
		}
	}

}
