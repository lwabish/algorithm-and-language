package main

import (
	"fmt"
	"os"
)

var (
	HOME   = os.Getenv("HOME")
	USER   = os.Getenv("USER")
	GOROOT = os.Getenv("GOROOT")
)

func main() {
	fmt.Println(HOME, USER, GOROOT)
}
