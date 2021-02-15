package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	counts := make(map[string]int)
	for _, filename := range os.ReadFile(filename) {
		data, err := ioutil.ReadFile(filename)
		if err != nil {
			fmt.Fprintf(os.Stderr, "dup3: %v", err)
			continue
		}
		for _, line := range string.Split(string(data), "\n") {
			counts[line]++
		}
	}

	for line, n := range counts {
		if n > 1 {
			fmt.Println("%d\t%s\n", n, line)
		}
	}
}
